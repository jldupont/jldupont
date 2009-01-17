"""
    Jean-Lou Dupont's Python library
    
    Installation
    ============
      Use I{easy_install jld} to install this library.
    
    Command-Line Tools
    ==================
      The following tools will be installed as scripts:
       - pypre.py [preprocessor based on Mako]
       - nsvn.py  [nuke svn]
       - dlc.py   [delicious backup]
       - mm.py    [mindmeister backup]
       - glf.py   [gliffy backup]
    
    @author: Jean-Lou Dupont
"""

__author__  = "Jean-Lou Dupont"
__version__ = "0.0.36"
__email__   = "python@jldupont.com"
__url__     = "http://www.jldupont.com/"
__desc__    = """ Jean-Lou Dupont's Python Library - WEB API & command line tools"""
__doc_url__ = "http://www.jldupont.com/doc/lib/jld/"

#
# must be in reStructuredText format (see http://docutils.sf.net/)
#
__long_desc__ = """

Content
=======

This library contains the following utilities:
  
* MindMeister_ mindmaps Backup command line: for exporting mindmaps from MindMeister_ in FreeMind format
  
  * EventManager script interface
  
* Delicious_ API & Backup command line utility

* Gliffy_ API & Backup command line utility

* Command-Line tools

  * pypre_   (preprocessor based on Mako_ , e.g. useful for pre-processing Apache config files)
  
  * nsvn_    (nuke svn: removes svn directories, e.g. useful under Windows where .dot files are difficult to handle)
 
* Cross-platform registry (Windows: uses the win32 registry, Linux: uses a filesystem path) 

.. _pypre: http://www.jldupont.com/doc/lib/jld/pypre

.. _nsvn: http://www.jldupont.com/doc/lib/jld/nsvn

.. _Mako: http://www.makotemplates.org/

.. _MindMeister: http://www.mindmeister.com/

.. _Gliffy: http://www.gliffy.com/

.. _Delicious: http://www.delicious.com/
"""

__dependencies__ = [] #listed throughout the individual modules

__classifiers__ = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: Public Domain',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    ]

# ==============================================
# ==============================================

if __name__ == "__main__":
    """ Tests
    """
    import os
    import webbrowser
    
    from docutils.core import publish_parts
    
    parts = publish_parts(source=__long_desc__, writer_name="html4css1")
    
    rendered_page = parts["html_title"] + parts["html_subtitle"] + parts["fragment"]

    cpath = os.path.dirname( __file__ )
    path = os.path.join(cpath, 'long_desc.html')
     
    file = open( path, "w" )
    file.write( rendered_page )
    file.close()

    url = "file://%s" % path
    webbrowser.open_new(url)
