/**
 * Code Syntax Highlighter.
 * Version 1.5.2
 * Copyright (C) 2004-2008 Alex Gorbatchev
 * http://www.dreamprojections.com/syntaxhighlighter/
 *
 *  This program is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, version 3 of the License.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

/*   
 * Erlang syntax contributed by Jean-Lou Dupont  http://www.jldupont.com/  
 */
dp.sh.Brushes.Erlang = function()
{
    var keywords = 'after and andalso band begin bnot bor bsl bsr bxor '+
    				'case catch cond div end fun if let not of or orelse '+
    				'query receive rem try when xor';

    var special =  '';

    this.regexList = [
        { regex: dp.sh.RegexLib.SingleLinePerlComments, css: 'comment' },
        { regex: new RegExp("^\\s*@\\w+", 'gm'), css: 'decorator' },
        { regex: new RegExp("(['\"]{3})([^\\1])*?\\1", 'gm'), css: 'comment' },
        { regex: new RegExp('"(?!")(?:\\.|\\\\\\"|[^\\""\\n\\r])*"', 'gm'), css: 'string' },
        { regex: new RegExp("'(?!')(?:\\.|(\\\\\\')|[^\\''\\n\\r])*'", 'gm'), css: 'string' },
        { regex: new RegExp("\\b\\d+\\.?\\w*", 'g'), css: 'number' },
        { regex: new RegExp(this.GetKeywords(keywords), 'gm'), css: 'keyword' },
        { regex: new RegExp(this.GetKeywords(special), 'gm'), css: 'special' }
        ];

    this.CssClass = 'dp-erl';
        this.Style =    '.dp-erl .builtins { color: #ff1493; }' +
                        '.dp-erl .magicmethods { color: #808080; }' +
                        '.dp-erl .exceptions { color: brown; }' +
                        '.dp-erl .types { color: brown; font-style: italic; }' +
                        '.dp-erl .commonlibs { color: #8A2BE2; font-style: italic; }';
};

dp.sh.Brushes.Erlang.prototype  = new dp.sh.Highlighter();
dp.sh.Brushes.Erlang.Aliases    = ['erl', 'erlang'];