/**
 * jld.js
 * 
 * @author Jean-Lou Dupont
 * @dependency jQuery
 */
 
if ( typeof JLD =="undefined" ) {

	// object literal
	//  Static class declaration
	var JLD = {};
	
	/**
	 * 
	 */
	JLD.copy = function( index ) {
		
		$('.JLD_FETCH_IFRAME').each(
			function() {
				// make sure we only do each iframe once
				status = this.getAttribute('status');
				if ( status == '1' )
					return;
				
				id= this.getAttribute('id');
				if ( index != id )
					return;
				
				content = this.contentDocument.body.textContent;
				$(this).after( "<div>" + content + '</div>' );
				this.setAttribute( 'status', '1');
			}
		);
	}
	
	/**
	 * DOM elements should be as follows:
	 * <tag class="JLD_FETCH" src="whatever-url"></tag>
	 */
	JLD.doFetches = function() {
		var index = 0;
		$(".JLD_FETCH").each(
			function() {
				src = this.getAttribute('src');
				$(this).append(
					"<iframe src='"+src+"' style='display:none' onload='JLD.copy("+index+");' class='JLD_FETCH_IFRAME' id='"+index+"' />"
				);
				index++;				
			}
		);
	}

	/**
	 * Should be called once the DOM is ready
	 */	
	JLD.init = function() {
		JLD.doFetches();
	}
}