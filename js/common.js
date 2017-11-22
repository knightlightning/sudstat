/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

$(document).ready(function () {
    checkUrl();
    setMenuSelection();
});

function setMenuSelection() {
    var pathname = window.location.pathname;
    $('.nav li > a[href="'+pathname+'"]').parent().addClass('active');
}

function checkUrl() {
    if (window.location.pathname === '/') {
        window.location.pathname += 'index.php';
    }
}

function setActive(list, item) {
    $('.active', list).removeClass('active');
    item.addClass('active');
}

function formatDate(str) {
    return str ? moment(new Date(str)).format("DD.MM.YYYY") : '';
}

function formatNull(val) {
    return val ? val : '';
}
//
//function getURLParam(name) {
//    var searchParams = new URLSearchParams(window.location.search);
//    return searchParams.get(name);
//}
//
//function fillMenu() {
//    if (sessionStorage.judges_stat_years && sessionStorage.courts_stat_years) {
//        $('#judges-stat-years').html(sessionStorage.judges_stat_years);
//        $('#courts-stat-years').html(sessionStorage.courts_stat_years);
//        setMenuSelection();
//    } else {
//         $.ajax({
//            url: '/cgi-bin/fetchstatyears.py',
//            processData: false,
//            contentType: false,
//            type: 'POST',
//            success: function (data) {
//                fetchStatYears(data);
//                setMenuSelection();
//            }
//        });
//    }
//}
//
//function fetchStatYears(data) {
//    var json = JSON.parse(data);
//    var html = '';
//    var curr_year = 0;
////    for (var j of json.stat_by_judges) {
////        if (curr_year !== j.year) {
////            curr_year = j.year;
////            if (html.length > 0) {
////                html += '</ul></li>';
////            }
////            html +=
////`<li class="dropdown-submenu">
////    <a class="submenu" href="#">${j.year} <span class="caret"></span></a>
////    <ul class="dropdown-menu">`;
////        }
////        html += `<li><a href="/judges-stat.php?y=${j.year}&q=${j.quarter}&id=${j.id}">${j.quarter}</a></li>`;
////    }
////    html += '</ul></li>';
////    sessionStorage.judges_stat_years = html;
////    $('#judges-stat-years').html(html);
//
//    html = '';
//    curr_year = 0;
//    for (var j of json.stat_by_courts) {
//        if (curr_year !== j.year) {
//            curr_year = j.year;
//            if (html.length > 0) {
//                html += '</ul></li>';
//            }
//            html +=
//`<li class="dropdown-submenu">
//    <a class="submenu" href="#">${j.year} <span class="caret"></span></a>
//    <ul class="dropdown-menu">`;
//        }
//        html += `<li><a href="/courts-stat.php?y=${j.year}&q=${j.quarter}&id=${j.id}">${j.quarter}</a></li>`;
//    }
//    html += '</ul></li>';
//    sessionStorage.courts_stat_years = html;
//    $('#courts-stat-years').html(html);
//}
//
////$(document).on('click', '.dropdown-submenu a.submenu', function(e){
////    $(this).next('ul').toggle();
////    e.stopPropagation();
////    e.preventDefault();
////});
