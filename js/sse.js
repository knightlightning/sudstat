/**
 * 
 */

function appendLog(msg) {
	$('#myprogress').html($('#myprogress').html() + msg);
	$("#myprogress").scrollTop($("#myprogress")[0].scrollHeight);
}

function clearLog() {
	$('#myprogress').html('');
}

function runSSE(script) {
	clearLog();
	var source = new EventSource(script);
	source.onmessage = function(event) {
		var data = JSON.parse(event.data);
		switch (data.type) {
			case 'info':
				//console.log(data.message);
				appendLog('<p class="sseinfo">' + data.timestamp + ' ' + data.message + '</p>');
				break;
				
			case 'error':
				//console.log(data.message);
				appendLog('<p class="sseerror">' + data.timestamp + ' ' + data.message + '</p>');
				break;
				
			case 'system':
				if ('END-OF-STREAM' == data.message) {
					//console.log('closing...');
			        source.close(); // stop retry
			    }
				break;
		}
	};
}
