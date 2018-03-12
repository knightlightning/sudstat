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
				appendLog('<p class="sseinfo">' + data.timestamp + ' ' + data.message + '</p>');
				break;
				
			case 'warning':
				appendLog('<p class="ssewarning">' + data.timestamp + ' ' + data.message + '</p>');
				break;
				
			case 'error':
				appendLog('<p class="sseerror">' + data.timestamp + ' ' + data.message + '</p>');
				break;
				
			case 'system':
				if ('END-OF-STREAM' == data.message) {
			        source.close(); // stop retry
			    }
				break;
		}
	};
}
