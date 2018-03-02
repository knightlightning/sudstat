/**
 * 
 */

$(document).ready(function () {
	var html = '';
	var currDate = new Date();
	for (year = currDate.getFullYear(); year > 2014; year--) {
		if (year == currDate.getFullYear()) {
			html += `<option value="${year}-${currDate.getMonth()+1}-${currDate.getDate()}">${year}</option>`;
		} else {
			html += `<option value="${year}-12-31">${year}</option>`;
		}
	}
	$('#statYear').html(html);
});

$(document).on('click', '#import', function () {
	var argv = $('#statYear').val();
	//console.log(argv);
	runSSE('/cgi-bin/adm/importjudgesstat.py?' + argv);
});
