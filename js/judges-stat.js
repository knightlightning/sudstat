/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

$(document).ready(function () {
    fetchCourts();
});

$(document).on('click', '#courts .list-group-item.selectable', function () {
    setActive($('#courts'), $(this));
    var court = $(`#courts a[href$=${$(this).parent().attr('id')}] div`).html();
    var stat_type = $(this).html();
    $('#current-selection').html(court + ' | ' + stat_type);
});

$(document).on('show.bs.collapse', '.collapse', function () {
    $('.glyphicon', $('#courts a[href$=' + this.id))
        .toggleClass('glyphicon-chevron-right')
        .toggleClass('glyphicon-chevron-down');
});

$(document).on('hide.bs.collapse', '.collapse', function () {
    $('.glyphicon', $('#courts a[href$=' + this.id))
        .toggleClass('glyphicon-chevron-down')
        .toggleClass('glyphicon-chevron-right');
});

function fetchCourts() {
    $.ajax({
        url: '/cgi-bin/fetchchargecourts.py',
        processData: false,
        contentType: false,
        type: 'POST',
        success: function (data) {
            fillCourts(data);
        }
    });
}

function fillCourts(data) {
    var courts = JSON.parse(data).courts;
    var html = "";
    var i = 0;
    for (var c of courts) {
        html +=
`<a href="#item-${i}" class="list-group-item" data-parent="#courts" data-toggle="collapse">
    <i class="glyphicon glyphicon-chevron-right"></i><div style="display:inline">${c.name}</div>
</a>
<div class="list-group collapse" id="item-${i}">
    <a href="javascript:void(0)" onclick="fetchJudgesCharge('${c.id}', 'adm')" class="list-group-item selectable small">АДМ</a>
    <a href="javascript:void(0)" onclick="fetchJudgesCharge('${c.id}', 'civ')" class="list-group-item selectable small">ГР</a>
    <a href="javascript:void(0)" onclick="fetchJudgesCharge('${c.id}', 'crim')" class="list-group-item selectable small">УГ</a>
</div>`;
        i = i+1;
    }
    $('#courtsList').html(html);
    $('#courtsList a').first().click();
    $('#courtsList .selectable').first().click();
}

function fetchJudgesCharge(c, type) {
    var data = new FormData();
    data.append('court_id', c);
    data.append('charge_type', type);
    $.ajax({
        url: '/cgi-bin/fetchjudgescharge.py',
        data: data,
        processData: false,
        contentType: false,
        type: 'POST',
        success: function (data) {
            fillJudgesCharge(data);
        }
    });
}

function fillJudgesCharge(data) {
    var json = JSON.parse(data);
    
    var thead = '<thead><tr><th>Судья</th>';
    for (var col of json.stat_columns) {
        thead += `<th>${col}</th>`;
    }
    thead += '</tr></thead>';
    
    var tbody = '<tbody>';
    charge = json.data;
    for (var i = 0; i < charge.length; i++) {
        tbody +=
`<tr class="subheader"><td colspan=${json.stat_columns.length+1}>
    ${charge[i].year} (актуальность данных на ${formatDate(charge[i].mod)})
</td></tr>`;
        var totals = Array(json.stat_columns.length).fill(0);
        for (var j = 0; j < charge[i].data.length; j++) {
            tbody += `<tr><td nowrap>${charge[i].data[j].name}</td>`;
            for (var k = 0; k < charge[i].data[j].stat.length; k++) {
                tbody += `<td>${formatNull(charge[i].data[j].stat[k])}</td>`;
                totals[k] += (charge[i].data[j].stat[k]);
            }
            tbody += '</tr>'
        }
        tbody += '<tr class="summary"><td>Итого</td>';
        for (var t of totals) {
            tbody += `<td>${t}</td>`;
        }
        tbody += '</tr>';
    }
    tbody += '</tbody>';
    
    $('#statData').html(thead + tbody);
}

//function fillCourts(data) {
//    var courts = JSON.parse(data).courts;
//    var thead = '<thead><tr><th rowspan="2">Суд</th>';
//    for (var i = 0; i < courts[0].data.length; i++) {
//        thead += `<th colspan="4">${courts[0].data[i].year}</th>`;
//    }
//    thead += '</tr><tr>';
//    for (var i = 0; i < courts[0].data.length; i++) {
//        thead += `<th>I</th><th>II</th><th>III</th><th>IV</th>`;
//    }
//    thead += '</tr></thead>';
//    var tbody = '<tbody>';
//    for (var c of courts) {
//        tbody += `<tr><td nowrap>${c.court}</td>`;
//        for (var year_data of c.data) {
//            for (var quarter_data of year_data.data) {
//                if (quarter_data) {
//                    tbody += `<td><a href="/resource/pdf/${quarter_data}">показать</a></td>`;
//                    //tbody += `<td><button type="button" class="btn btn-link">${quarter_data}</button></td>`;
//                } else {
//                    tbody +=
//`<td nowrap style="padding: 2px;"><div style="margin:0;padding: 0px 3px;" class="alert alert-warning" role="alert">
//    <span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>
//    нет данных
//</div></td>`;
//                }
//            }
//        }
//        tbody += '</tr>';
//    }
//    tbody += '</tbody>';
//    $('#statData').html(thead + tbody);
////    var html = '';
////    for (var c of courts) {
////        html += `<a href="javascript:void(0)" onclick="changeData('${c.name}')" class="list-group-item">${c.name}</a>`;
////    }
////    $('#courtsList').html(html);
//}
//
//$(document).on('click', '#statData a', function (e) {
//    e.preventDefault();
//    $('#myModal #modalContent').html(`<object data="/resource/pdf/test1.pdf" type="application/pdf" width="100%" height="100%"></object>`);
//    $('#myModal #caption').html('caption');
//    $('#myModal').show();
//});
//
//$(document).on('click', '.myavatar', function () {
//
//});
//
//$(document).on('click', '#myModal .close', function () {
//    $('#myModal').hide();
//});
