/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

$(document).ready(function () {
    var html = '';
    var date = new Date();
    for (var y = date.getFullYear(); y > 2000; y--) {
        html += `<option value="${y}">${y}</option>`;
    }
    $('#statYear').html(html);
    var q = Math.ceil(date.getMonth()/3) - 1;
    $('#statQuarter').prop('selectedIndex', q);
    $("#statType").prop('selectedIndex', -1);
});

$(document).on('submit', '#myForm', function (event) {
    event.preventDefault();
    var fd = new FormData();
    fd.append("stat_type", $("#statType").val());
    fd.append("year", $("#statYear").val());
    fd.append("quarter", $("#statQuarter").val());
    fd.append("file", $("#file").prop('files')[0]);
    $.ajax({
        url: '/wsgi-bin/uploadstatfile',
        data: fd,
        processData: false,
        contentType: false,
        type: 'POST',
        success: function (data) {
            //console.log('success');
        },
        error: function (data) {
            alert(data);
        }
    });
});

function enableUpload() {
    var statType = $("#statType").prop("selectedIndex");
    var file = $("#file").val();
    $("#myForm :submit").prop("disabled", !file || statType === -1);
}

$(document).on('change', '#statType', function () {
    enableUpload();
});

$(document).on('change', '#file', function () {
    const MAX_FILE_SIZE = 50 * 1024 * 1024;
    var f = this.files[0];
    if (f.size > MAX_FILE_SIZE) {
        alert("Файл \"" + f.name + "\" превышает установленный лимит (50 МБ).");
        this.value = "";
    }
    enableUpload();
});
