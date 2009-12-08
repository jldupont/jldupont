/**
 * @title  Chrome Extension: Auto-Reload
 * @file   content.js
 * @author Jean-Lou Dupont
 * @desc   Content Script
 */

var timer_id;
var port;
var default_inter=30;
var default_randomize=0;
var default_disabled_time_range=false;
var default_begin_hour=23;
var default_end_hour=6;
var default_begin_min=0;
var default_end_min=30;

function checkTimeRange(tr) {
	var cdate=new Date();
	var ch= cdate.getHours();
	var cm= cdate.getMinutes();
	var ct=(ch*60)+cm;
	
	var bt=tr.begin_hour*60 + tr.begin_min;
	var et=tr.end_hour*60   + tr.end_min;
	
	console.log("current: "+ ch + ":"+ cm + "("+ct+")");
	console.log("begin_hour: "+tr.begin_hour+", begin_min: "+tr.begin_min);
	console.log("end_hour: "+tr.end_hour+", end_min: "+tr.end_min);
	console.log("bt: "+bt+" , et: "+et);
	
	return (ct >= bt) && (ct <= et);
}


function reloader(cmd) {

	var state     = cmd.state     || false;
	var timeout   = cmd.timeout   || default_inter;
	var randomize = cmd.randomize || default_randomize;
	var disabled_time_range = cmd.disabled_time_range || default_disabled_time_range;
	
	var time_range = {
		begin_hour: cmd.begin_hour || default_begin_hour,
		begin_min:  cmd.begin_min  || default_begin_min,
		end_hour:   cmd.end_hour   || default_end_hour,
		end_min:    cmd.end_min    || default_end_min		
	};
	
	timeout = timeout * 1000;
	console.log("Base timeout: " + timeout + ", randomize (%): "+ randomize);
	
	timeout = timeout + timeout * (randomize/100 * Math.random());
	console.log("Randomize timeout: "+timeout);
	
	//we already are waiting to be reloaded
	if (state && timer_id) 
		return;
	
	if (state) {
		timer_id=setTimeout(function() {
			
			// is there a "disabled_time_range" active?
			if (disabled_time_range != false) {
				if (checkTimeRange(time_range))
					window.location.reload(true);
			} else {
				window.location.reload(true);	
			}
		}, timeout );
		
		console.log(" > auto-reload: scheduled in "+timeout+" ms.");
	} else {
		if (timer_id) {
			clearInterval(timer_id);
			timer_id=undefined;
		}
		console.log(" > auto-reload: none scheduled");
	}
}//

port=chrome.extension.connect();
port.onMessage.addListener(reloader);
