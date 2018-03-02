/**
 * kmironov
 */

$(document).ready(function () {
});

$(document).on('click', '#import', function () {
	var argv = $('#importOblsudData').is(":checked") ? '?obl:' : '?:';
	argv += $('#importRaisudData').is(":checked") ? 'rai:' : ':';
	argv += $('#deleteInputFiles').is(":checked") ? 'delete' : '';
	runSSE('/cgi-bin/adm/importjudges.py' + argv);
});

$(document).on('change', '#importOblsudData, #importRaisudData', function () {
	$('#import').prop('disabled', !($('#importOblsudData').is(":checked") || $('#importRaisudData').is(":checked")));
});
