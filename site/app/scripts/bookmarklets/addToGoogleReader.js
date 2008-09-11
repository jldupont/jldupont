/**
 * addToGoogleReader
 * 
 * @author: Jean-Lou Dupont 
 */

 // find out if the script is already loaded on the current page
 
 if ( 'undefined' == typeof jld ) {
 	
 	// object literal
 	var jld = {
 	
 		run: function() {
 			var links = document.getElementsByTagName("link");
 			
 			// nothing here
 			if ( null != links ) {
	 			for(var i=0;i<links.length;i++) {
	 				var type = links[i].getAttribute("type");
	 				if (("application/rss+xml" == type) || ("application/atom+xml") == type) {
	 					var href = links[i].getAttribute("href");
	 					document.location = "http://www.google.com/ig/add?feedurl=" + href;
	 				}
	 			}
 			}
 			
 			// fall-through if no feed is found
 			alert( 'No feed link found!' );
 		}
 	
 	};
 	
 }
 
 //Execute!
 jld.run();
 