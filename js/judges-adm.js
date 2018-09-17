/**
 * kmironov
 */

$(document).ready(function () {
});

$(document).on('click', '#import', function () {
	var argv = $('#importOblsudData').is(":checked") ? 'True/' : 'False/';
	argv += $('#importRaisudData').is(":checked") ? 'True/' : 'False/';
	argv += $('#deleteInputFiles').is(":checked") ? 'True/' : 'False';
	runSSE('/wsgi-bin/importjudges/' + argv);
});

$(document).on('change', '#importOblsudData, #importRaisudData', function () {
	$('#import').prop('disabled', !($('#importOblsudData').is(":checked") || $('#importRaisudData').is(":checked")));
});
