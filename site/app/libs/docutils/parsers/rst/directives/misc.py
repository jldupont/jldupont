# $Id$
# Authors: David Goodger <goodger@python.org>; Dethe Elza
# Copyright: This module has been placed in the public domain.

"""Miscellaneous directives."""

__docformat__ = 'reStructuredText'

import sys
import os.path
import re
import time
from docutils import io, nodes, statemachine, utils
from docutils.parsers.rst import Directive, convert_directive_function
from docutils.parsers.rst import directives, roles, states
from docutils.transforms import misc


class Include(Directive):

    """
    Include content read from a separate source file.

    Content may be parsed by the parser, or included as a literal
    block.  The encoding of the included file can be specified.  Only
    a part of the given file argument may be included by specifying
    text to match before and/or after the text to be used.
    """

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {'literal': directives.flag,
                   'encoding': directives.encoding,
                   'start-after': directives.unchanged_required,
                   'end-before': directives.unchanged_required}

    standard_include_path = os.path.join(os.path.dirname(states.__file__),
                                         'include')

    def run(self):
        """Include a reST file as part of the content of this reST file."""
        if not self.state.document.settings.file_insertion_enabled:
            raise self.warning('"%s" directive disabled.' % self.name)
        source = self.state_machine.input_lines.source(
            self.lineno - self.state_machine.input_offset - 1)
        source_dir = os.path.dirname(os.path.abspath(source))
        path = directives.path(self.arguments[0])
        if path.startswith('<') and path.endswith('>'):
            path = os.path.join(self.standard_include_path, path[1:-1])
        path = os.path.normpath(os.path.join(source_dir, path))
        path = utils.relative_path(None, path)
        encoding = self.options.get(
            'encoding', self.state.document.settings.input_encoding)
        try:
            self.state.document.settings.record_dependencies.add(path)
            include_file = io.FileInput(
                source_path=path, encoding=encoding,
                error_handler=(self.state.document.settings.\
                               input_encoding_error_handler),
                handle_io_errors=None)
        except IOError, error:
            raise self.severe('Problems with "%s" directive path:\n%s: %s.'
                              % (self.name, error.__class__.__name__, error))
        try:
            include_text = include_file.read()
        except UnicodeError, error:
            raise self.severe(
                'Problem with "%s" directive:\n%s: %s'
                % (self.name, error.__class__.__name__, error))
        # start-after/end-before: no restrictions on newlines in match-text,
        # and no restrictions on matching inside lines vs. line boundaries
        after_text = self.options.get('start-after', None)
        if after_text:
            # skip content in include_text before *and incl.* a matching text
            after_index = include_text.find(after_text)
            if after_index < 0:
                raise self.severe('Problem with "start-after" option of "%s" '
                                  'directive:\nText not found.' % self.name)
            include_text = include_text[after_index + len(after_text):]
        before_text = self.options.get('end-before', None)
        if before_text:
            # skip content in include_text after *and incl.* a matching text
            before_index = include_text.find(before_text)
            if before_index < 0:
                raise self.severe('Problem with "end-before" option of "%s" '
                                  'directive:\nText not found.' % self.name)
            include_text = include_text[:before_index]
        if self.options.has_key('literal'):
            literal_block = nodes.literal_block(include_text, include_text,
                                                source=path)
            literal_block.line = 1
            return [literal_block]
        else:
            include_lines = statemachine.string2lines(include_text,
                                                      convert_whitespace=1)
            self.state_machine.insert_input(include_lines, path)
            return []


class Raw(Directive):

    """
    Pass through content unchanged

    Content is included in output based on type argument

    Content may be included inline (content section of directive) or
    imported from a file or url.
    """

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {'file': directives.path,
                   'url': directives.uri,
                   'encoding': directives.encoding}
    has_content = True

    def run(self):
        if (not self.state.document.settings.raw_enabled
            or (not self.state.document.settings.file_insertion_enabled
                and (self.options.has_key('file')
                     or self.options.has_key('url')))):
            raise self.warning('"%s" directive disabled.' % self.name)
        attributes = {'format': ' '.join(self.arguments[0].lower().split())}
        encoding = self.options.get(
            'encoding', self.state.document.settings.input_encoding)
        if self.content:
            if self.options.has_key('file') or self.options.has_key('url'):
                raise self.error(
                    '"%s" directive may not both specify an external file '
                    'and have content.' % self.name)
            text = '\n'.join(self.content)
        elif self.options.has_key('file'):
            if self.options.has_key('url'):
                raise self.error(
                    'The "file" and "url" options may not be simultaneously '
                    'specified for the "%s" directive.' % self.name)
            source_dir = os.path.dirname(
                os.path.abspath(self.state.document.current_source))
            path = os.path.normpath(os.path.join(source_dir,
                                                 self.options['file']))
            path = utils.relative_path(None, path)
            try:
                self.state.document.settings.record_dependencies.add(path)
                raw_file = io.FileInput(
                    source_path=path, encoding=encoding,
                    error_handler=(self.state.document.settings.\
                                   input_encoding_error_handler),
                    handle_io_errors=None)
            except IOError, error:
                raise self.severe('Problems with "%s" directive path:\n%s.'
                                  % (self.name, error))
            try:
                text = raw_file.read()
            except UnicodeError, error:
                raise self.severe(
                    'Problem with "%s" directive:\n%s: %s'
                    % (self.name, error.__class__.__name__, error))
            attributes['source'] = path
        elif self.options.has_key('url'):
            source = self.options['url']
            # Do not import urllib2 at the top of the module because
            # it may fail due to broken SSL dependencies, and it takes
            # about 0.15 seconds to load.
            import urllib2
            try:
                raw_text = urllib2.urlopen(source).read()
            except (urllib2.URLError, IOError, OSError), error:
                raise self.severe(
                    'Problems with "%s" directive URL "%s":\n%s.'
                    % (self.name, self.options['url'], error))
            raw_file = io.StringInput(
                source=raw_text, source_path=source, encoding=encoding,
                error_handler=(self.state.document.settings.\
                               input_encoding_error_handler))
            try:
                text = raw_file.read()
            except UnicodeError, error:
                raise self.severe(
                    'Problem with "%s" directive:\n%s: %s'
                    % (self.name, error.__class__.__name__, error))
            attributes['source'] = source
        else:
            # This will always fail because there is no content.
            self.assert_has_content()
        raw_node = nodes.raw('', text, **attributes)
        return [raw_node]


class Replace(Directive):

    has_content = True

    def run(self):
        if not isinstance(self.state, states.SubstitutionDef):
            raise self.error(
                'Invalid context: the "%s" directive can only be used within '
                'a substitution definition.' % self.name)
        self.assert_has_content()
        text = '\n'.join(self.content)
        element = nodes.Element(text)
        self.state.nested_parse(self.content, self.content_offset,
                                element)
        if ( len(element) != 1
             or not isinstance(element[0], nodes.paragraph)):
            messages = []
            for node in element:
                if isinstance(node, nodes.system_message):
                    node['backrefs'] = []
                    messages.append(node)
            error = self.state_machine.reporter.error(
                'Error in "%s" directive: may contain a single paragraph '
                'only.' % (self.name), line=self.lineno)
            messages.append(error)
            return messages
        else:
            return element[0].children


class Unicode(Directive):

    r"""
    Convert Unicode character codes (numbers) to characters.  Codes may be
    decimal numbers, hexadecimal numbers (prefixed by ``0x``, ``x``, ``\x``,
    ``U+``, ``u``, or ``\u``; e.g. ``U+262E``), or XML-style numeric character
    entities (e.g. ``&#x262E;``).  Text following ".." is a comment and is
    ignored.  Spaces are ignored, and any other text remains as-is.
    """

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {'trim': directives.flag,
                   'ltrim': directives.flag,
                   'rtrim': directives.flag}

    comment_pattern = re.compile(r'( |\n|^)\.\. ')

    def run(self):
        if not isinstance(self.state, states.SubstitutionDef):
            raise self.error(
                'Invalid context: the "%s" directive can only be used within '
                'a substitution definition.' % self.name)
        substitution_definition = self.state_machine.node
        if self.options.has_key('trim'):
            substitution_definition.attributes['ltrim'] = 1
            substitution_definition.attributes['rtrim'] = 1
        if self.options.has_key('ltrim'):
            substitution_definition.attributes['ltrim'] = 1
        if self.options.has_key('rtrim'):
            substitution_definition.attributes['rtrim'] = 1
        codes = self.comment_pattern.split(self.arguments[0])[0].split()
        element = nodes.Element()
        for code in codes:
            try:
                decoded = directives.unicode_code(code)
            except ValueError, err:
                raise self.error(
                    'Invalid character code: %s\n%s: %s'
                    % (code, err.__class__.__name__, err))
            element += nodes.Text(decoded)
        return element.children


class Class(Directive):

    """
    Set a "class" attribute on the directive content or the next element.
    When applied to the next element, a "pending" element is inserted, and a
    transform does the work later.
    """

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True

    def run(self):
        try:
            class_value = directives.class_option(self.arguments[0])
        except ValueError:
            raise self.error(
                'Invalid class attribute value for "%s" directive: "%s".'
                % (self.name, self.arguments[0]))
        node_list = []
        if self.content:
            container = nodes.Element()
            self.state.nested_parse(self.content, self.content_offset,
                                    container)
            for node in container:
                node['classes'].extend(class_value)
            node_list.extend(container.children)
        else:
            pending = nodes.pending(
                misc.ClassAttribute,
                {'class': class_value, 'directive': self.name},
                self.block_text)
            self.state_machine.document.note_pending(pending)
            node_list.append(pending)
        return node_list


class Role(Directive):

    has_content = True

    argument_pattern = re.compile(r'(%s)\s*(\(\s*(%s)\s*\)\s*)?$'
                                  % ((states.Inliner.simplename,) * 2))

    def run(self):
        """Dynamically create and register a custom interpreted text role."""
        if self.content_offset > self.lineno or not self.content:
            raise self.error('"%s" directive requires arguments on the first '
                             'line.' % self.name)
        args = self.content[0]
        match = self.argument_pattern.match(args)
        if not match:
            raise self.error('"%s" directive arguments not valid role names: '
                             '"%s".' % (self.name, args))
        new_role_name = match.group(1)
        base_role_name = match.group(3)
        messages = []
        if base_role_name:
            base_role, messages = roles.role(
                base_role_name, self.state_machine.language, self.lineno,
                self.state.reporter)
            if base_role is None:
                error = self.state.reporter.error(
                    'Unknown interpreted text role "%s".' % base_role_name,
                    nodes.literal_block(self.block_text, self.block_text),
                    line=self.lineno)
                return messages + [error]
        else:
            base_role = roles.generic_custom_role
        assert not hasattr(base_role, 'arguments'), (
            'Supplemental directive arguments for "%s" directive not '
            'supported (specified by "%r" role).' % (self.name, base_role))
        try:
            converted_role = convert_directive_function(base_role)
            (arguments, options, content, content_offset) = (
                self.state.parse_directive_block(
                self.content[1:], self.content_offset, converted_role,
                option_presets={}))
        except states.MarkupError, detail:
            error = self.state_machine.reporter.error(
                'Error in "%s" directive:\n%s.' % (self.name, detail),
                nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno)
            return messages + [error]
        if not options.has_key('class'):
            try:
                options['class'] = directives.class_option(new_role_name)
            except ValueError, detail:
                error = self.state_machine.reporter.error(
                    'Invalid argument for "%s" directive:\n%s.'
                    % (self.name, detail), nodes.literal_block(
                    self.block_text, self.block_text), line=self.lineno)
                return messages + [error]
        role = roles.CustomRole(new_role_name, base_role, options, content)
        roles.register_local_role(new_role_name, role)
        return messages


class DefaultRole(Directive):

    """Set the default interpreted text role."""

    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = False

    def run(self):
        if not self.arguments:
            if roles._roles.has_key(''):
                # restore the "default" default role
                del roles._roles['']
            return []
        role_name = self.arguments[0]
        role, messages = roles.role(role_name, self.state_machine.language,
                                    self.lineno, self.state.reporter)
        if role is None:
            error = self.state.reporter.error(
                'Unknown interpreted text role "%s".' % role_name,
                nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno)
            return messages + [error]
        roles._roles[''] = role
        # @@@ should this be local to the document, not the parser?
        return messages


class Title(Directive):

    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True

    def run(self):
        self.state_machine.document['title'] = self.arguments[0]
        return []


class Date(Directive):

    has_content = True

    def run(self):
        if not isinstance(self.state, states.SubstitutionDef):
            raise self.error(
                'Invalid context: the "%s" directive can only be used within '
                'a substitution definition.' % self.name)
        format = '\n'.join(self.content) or '%Y-%m-%d'
        text = time.strftime(format)
        return [nodes.Text(text)]


class TestDirective(Directive):

    """This directive is useful only for testing purposes."""

    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {'option': directives.unchanged_required}
    has_content = True

    def run(self):
        if self.content:
            text = '\n'.join(self.content)
            info = self.state_machine.reporter.info(
                'Directive processed. Type="%s", arguments=%r, options=%r, '
                'content:' % (self.name, self.arguments, self.options),
                nodes.literal_block(text, text), line=self.lineno)
        else:
            info = self.state_machine.reporter.info(
                'Directive processed. Type="%s", arguments=%r, options=%r, '
                'content: None' % (self.name, self.arguments, self.options),
                line=self.lineno)
        return [info]

# Old-style, functional definition:
#
# def directive_test_function(name, arguments, options, content, lineno,
#                             content_offset, block_text, state, state_machine):
#     """This directive is useful only for testing purposes."""
#     if content:
#         text = '\n'.join(content)
#         info = state_machine.reporter.info(
#             'Directive processed. Type="%s", arguments=%r, options=%r, '
#             'content:' % (name, arguments, options),
#             nodes.literal_block(text, text), line=lineno)
#     else:
#         info = state_machine.reporter.info(
#             'Directive processed. Type="%s", arguments=%r, options=%r, '
#             'content: None' % (name, arguments, options), line=lineno)
#     return [info]
#
# directive_test_function.arguments = (0, 1, 1)
# directive_test_function.options = {'option': directives.unchanged_required}
# directive_test_function.content = 1
