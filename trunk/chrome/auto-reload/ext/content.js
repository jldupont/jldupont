/**
 * @author: Jean-Lou Dupont
 *  Auto-Reload: Content.js
 */
 
function reloader() {
	window.location.reload(true);
}
 
port=chrome.extension.connect();
port.onMessage.addListener(reloader);
