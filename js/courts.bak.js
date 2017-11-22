/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

$(document).ready(function () {
    if (sessionStorage.courts) {
        $('#courtsList').html(sessionStorage.courts);
        setSelection();
    } else {
        $.ajax({
            url: '/cgi-bin/fetchjobplaces.py',
            processData: false,
            contentType: false,
            type: 'POST',
            success: function (data) {
                fillCourts(data);
                setSelection();
            }
        });
    }
});

function setSelection() {
    if (window.location.search) {
        $('#courts').scrollTop(sessionStorage.courtsScroll);
        
        var court = getURLParam('c');
        var courtType = getURLParam('t');
        fetchJudges(court, courtType);
        
        var path = window.location.pathname + window.location.search;
        var item = $(`#courts a[href="${path}"]`);
        $(`#courts a[href$="${item.parent().attr('id')}"]`).trigger('click');
        setActive($('#courts'), item);
        
        var pageName = decodeURIComponent(court);
        switch (decodeURIComponent(courtType)) {
            case 'obl':
            case 'fed':
                pageName += ' | федеральные судьи';
                break;
            case 'mir':
                pageName += ' | мировые судьи';
                break;
        }
        $('#current-selection').html(pageName);
    } else {
        var href = $('#courtsList a').first().attr('href');
        window.location.href = href;
    }
}

function fillCourts(data) {
    var job_places = JSON.parse(data).job_places;
    var html = `<a href="javascript:void(0)" onclick="fetchJudges('Омский областной суд', 'obl')" class="list-group-item selectable">Областной суд</a>`;
    [
        'Кировский районный суд',
        'Куйбышевский районный суд',
        'Ленинский районный суд',
        'Октябрьский районный суд',
        'Первомайский районный суд',
        'Советский районный суд',
        'Центральный районный суд',
        'Азовский районный суд',
        'Большереченский районный суд',
        'Большеуковский районный суд',
        'Горьковский районный суд',
        'Знаменский районный суд',
        'Исилькульский городской суд',
        'Калачинский городской суд',
        'Колосовский районный суд',
        'Кормиловский районный суд',
        'Крутинский районный суд',
        'Любинский районный суд',
        'Марьяновский районный суд',
        'Москаленский районный суд',
        'Муромцевский районный суд',
        'Называевский городской суд',
        'Нижнеомский районный суд',
        'Нововаршавский районный суд',
        'Одесский районный суд',
        'Оконешниковский районный суд',
        'Омский районный суд',
        'Павлоградский районный суд',
        'Полтавский районный суд',
        'Русско-Полянский районный суд',
        'Саргатский районный суд',
        'Седельниковский районный суд',
        'Таврический районный суд',
        'Тарский городской суд',
        'Тевризский районный суд',
        'Тюкалинский городской суд',
        'Усть-Ишимский районный суд',
        'Черлакский районный суд',
        'Шербакульский районный суд',
        '61 гарнизонный военный суд',
        'Омский гарнизонный военный суд'
    ].forEach(function (e, i, arr) {
        if (job_places.filter(function (j) {
            return j.name.indexOf(e) !== -1 || j.name === e;
        }).length > 0) {
            html +=
`<a href="#item-${i}" class="list-group-item" data-parent="#courts" data-toggle="collapse">
    <i class="glyphicon glyphicon-chevron-right"></i>${e}
</a>
<div class="list-group collapse" id="item-${i}">
    <a href="javascript:void(0)" onclick="fetchJudges('${e}', 'fed')" class="list-group-item selectable small">Федеральные судьи</a>`;

//`<a href="#item-${i}" class="list-group-item" data-parent="#courts" data-toggle="collapse">
//    <i class="glyphicon glyphicon-chevron-right"></i>${e}
//</a>
//<div class="list-group collapse" id="item-${i}">
//    <a href="/index.php?c=${encodeURIComponent(e)}&t=fed" class="list-group-item selectable small">Федеральные судьи</a>`;

            if (e.indexOf('военный') === -1) {
                var court = 'в ' + e.split(' ')[0];
                var mir_count = job_places.filter(function (j) {
                    return j.name.indexOf(court.substring(0, court.length-2)) > 0;
                }).length;
                if (mir_count > 0) {
                    html +=
//`   <a href="/index.php?c=${encodeURIComponent(e)}&t=mir" class="list-group-item selectable small">Мировые судьи</a>`;
`   <a href="javascript:void(0)" onclick="fetchJudges('${e}', 'mir')" class="list-group-item selectable small">Мировые судьи</a>`;
                }
            }

            html += '</div>';
        }
    });
    sessionStorage.courts = html;
    $('#courtsList').html(html);
}

