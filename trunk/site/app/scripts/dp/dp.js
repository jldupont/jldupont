/**
 * Uses the syntax highlighter found
 * at http://code.google.com/p/syntaxhighlighter/
 * 
 * Usage:
 * 
 * <textarea name="code" class="js" rows="20" cols="70">
 *   // place JS code here
 * </textarea>
 * 
 * <script language="javascript" src="http://www.jldupont.com/scripts/dp/shCore.js"></script>
 * <script class="javascript" src="http://www.jldupont.com/scripts/dp/shBrushJScript.js"></script>
 * <script class="javascript" src="http://www.jldupont.com/scripts/dp/dp.js"></script>
 * 
 * @author Jean-Lou Dupont
 * @version 0.2
 */
dp.SyntaxHighlighter.BloggerMode();
dp.SyntaxHighlighter.ClipboardSwf = 'http://www.jldupont.com/scripts/clipboard.swf';
dp.SyntaxHighlighter.HighlightAll('code');
document.write('<link type="text/css" rel="stylesheet" href="http://www.jldupont.com/scripts/dp/SyntaxHighlighter.css">');
