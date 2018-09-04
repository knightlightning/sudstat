$(document).ready(function () {
    if (sessionStorage.courts) {
        $('#courtsList').html(sessionStorage.courts);
        setSelection();
    } else {
        $.ajax({
            url: '/wsgi-bin/fetchjobplaces',
            processData: false,
            contentType: false,
            type: 'GET',
            success: function (data) {
                fillCourts(data);
                setSelection();
            }
        });
    }
});

function setSelection() {
    $('#courtsList .selectable').first().click();
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

            if (e.indexOf('военный') === -1) {
                var court = 'в ' + e.split(' ')[0];
                var mir_count = job_places.filter(function (j) {
                    return j.name.indexOf(court.substring(0, court.length-2)) > 0;
                }).length;
                if (mir_count > 0) {
                    html +=
`   <a href="javascript:void(0)" onclick="fetchJudges('${e}', 'mir')" class="list-group-item selectable small">Мировые судьи</a>`;
                }
            }

            html += '</div>';
        }
    });
    sessionStorage.courts = html;
    $('#courtsList').html(html);
}

function fetchJudges(court, type) {
    var data = new FormData();
    data.append('court', court);
    data.append('type', type);
    $.ajax({
        url: '/wsgi-bin/fetchjudges',
        data: data,
        processData: false,
        contentType: false,
        type: 'POST',
        success: function (data) {
            fillJudges(data);
        }
    });
    
    var pageName = court;
    switch (type) {
        case 'obl':
        case 'fed':
            pageName += ' | федеральные судьи';
            break;
        case 'mir':
            pageName += ' | мировые судьи';
            break;
    }
    $('#current-selection').html(pageName);
}

function fillJudges(data) {
    var html = '';
    for (var j of JSON.parse(data).judges) {
        html +=
`<a href="javascript:void(0)" onclick="fetchJudgeInfo('${j.id}')" class="media list-group-item">
    <div class="media-left">
        <img src="resource/img/${j.avatar ? j.avatar : 'no-avatar.png'}" class="media-object myavatar" style="width:80px">
    </div>
    <div class="media-body">
        <h4 class="media-heading">${j.surname} ${j.name} ${j.patron}</h4>
        <p>${j.job_position}</p>
        <div class="mymedia-footer">
            <p class="small"><i>Актуальность данных на ${formatDate(j.upload_date)}</i></p>
        </div>
    </div>
</a>`;
    }
    $('#usersPanel').html(html);
    $('#usersPanel a').first().click();
}

function fetchJudgeInfo(id) {
    var data = new FormData();
    data.append('judge_id', id);
    $.ajax({
        url: '/wsgi-bin/fetchjudgeinfo',
        data: data,
        processData: false,
        contentType: false,
        type: 'POST',
        success: function (data) {
            fillJudgeInfo(data);
        }
    });
}

function calcExp(date, y, m, d) {
    var diff = moment(new Date()).diff(moment(new Date(date)));
    var dur = moment.duration(diff);
    dur.add(y, 'y');
    dur.add(m, 'M');
    dur.add(d, 'd');
    return [dur.years(), dur.months(), dur.days()];
}

function fillJudgeInfo(data) {
    json = JSON.parse(data);
    $('#judgefio tbody').html(
            `<tr class="data">
    <td>Фамилия</td>
    <td>${json.judge.surname}</td>
</tr>
<tr class="data">
    <td>Имя</td>
    <td>${json.judge.name}</td>
</tr>
<tr class="data">
    <td>Отчество</td>
    <td>${json.judge.patron}</td>
</tr>
<tr class="data">
    <td style="min-width:130px;">Дата рождения</td>
    <td>${formatDate(json.judge.birthdate)}</td>
</tr>
<tr class="data">
    <td>Место рождения</td>
    <td>${json.judge.birthplace}</td>
</tr>
<tr class="data">
    <td>Гражданство</td>
    <td>${json.judge.citizenship}</td>
</tr>`);

    if (json.judge.qualifier_class_name) {
        $('#judge-qualification tbody').html(
                `<tr class="data">
        <td>Класс</td>
        <td>${json.judge.qualifier_class_name}</td>
    </tr>
    <tr class="data">
        <td>Приказ</td>
        <td>${json.judge.qualifier_class_reason}</td>
    </tr>
    <tr class="data">
        <td>Дата</td>
        <td>${formatDate(json.judge.qualifier_class_date)}</td>
    </tr>`);
        $('#judge-qualification').show();
    } else {
        $('#judge-qualification').hide();
    }

    $('#judge-assignment tbody').html(
`<tr class="data">
    <td>Приказ</td>
    <td>${json.judge.assignment_order}</td>
</tr>
<tr class="data">
    <td>Дата</td>
    <td>${formatDate(json.judge.assignment_date)}</td>
</tr>`);

    var html = "";
    for (var e of json.educations) {
        html +=
`<tr class="data">
    <td>ВУЗ</td>
    <td>${e.school}</td>
</tr>
<tr class="data">
    <td>Тип</td>
    <td>${formatNull(e.type)}</td>
</tr>
<tr class="data">
    <td>Диплом</td>
    <td>${formatDate(e.graduation_date)}</td>
</tr>
<tr class="data">
    <td>Специализация</td>
    <td>${formatNull(e.specialization)}</td>
</tr>
<tr class="data">
    <td>Квалификация</td>
    <td>${formatNull(e.qualification)}</td>
</tr>`;
    }
    $('#educations tbody').html(html);

    if (json.degrees.length === 0) {
        $('#degrees').hide();
    } else {
        html = "";
        for (var d of json.degrees) {
            html +=
`<tr class="data">
    <td>Степень</td>
    <td>${d.name}</td>
</tr>
<tr class="data">
    <td>Приказ</td>
    <td>${d.order_text}</td>
</tr>
<tr class="data">
    <td>Дата</td>
    <td>${formatDate(d.order_date)}</td>
</tr>`;
        }
        $('#degrees tbody').html(html);
        $('#degrees').show();
    }

    if (json.awards.length === 0) {
        $('#awards').hide();
    } else {
        html = "";
        for (var a of json.awards) {
            html +=
`<tr class="data">
    <td>Награда</td>
    <td>${a.name}</td>
</tr>
<tr class="data">
    <td>Документ</td>
    <td>${a.certificate_type}</td>
</tr>
<tr class="data">
    <td>Номер</td>
    <td>${a.certificate_number}</td>
</tr>
<tr class="data">
    <td>Дата</td>
    <td>${formatDate(a.certificate_date)}</td>
</tr>`;
        }
        $('#awards tbody').html(html);
        $('#awards').show();
    }

    html = "";
    for (var j of json.jobs) {
        html +=
                `<tr class="data">
    <td>${formatDate(j.acceptance_date)}</td>
    <td>${formatDate(j.discharge_date)}</td>
    <td>${j.place}</td>
    <td>${j.position}</td>
    <td>${formatNull(j.city)}</td>
</tr>`;
    }
    $('#jobs tbody').html(html);

    judge_exp = calcExp(json.judge.job_acceptance_day, json.judge.previous_judge_exp_years, json.judge.previous_judge_exp_months, json.judge.previous_judge_exp_days);
    law_exp = calcExp(json.judge.job_acceptance_day, json.judge.previous_law_exp_years, json.judge.previous_law_exp_months, json.judge.previous_law_exp_days);
    $('#judge-exp tbody').html(
`<tr class="data">
    <td class="subtitle-left">В должности судьи</td>
    <td>${judge_exp[0]}</td>
    <td>${judge_exp[1]}</td>
    <td>${judge_exp[2]}</td>
</tr>
<tr class="data">
    <td class="subtitle-left">В области юриспруденции</td>
    <td>${law_exp[0]}</td>
    <td>${law_exp[1]}</td>
    <td>${law_exp[2]}</td>
</tr>`);
}

$(document).on('click', '#courtsList .selectable', function () {
    setActive($('#courtsList'), $(this));
});

$(document).on('click', '#usersPanel .list-group-item', function () {
    setActive($('#usersPanel'), $(this));
});

$(document).on('click', '.myavatar', function () {
    $('#myModal #modalContent').html(`<img class="avatar-popup" src="${$(this).attr('src')}">`);
    $('#myModal #caption').html($('h4', $(this).parents('.list-group-item')).html());
    $('#myModal').show();
});

$(document).on('click', '#myModal .close', function () {
    $('#myModal').hide();
});
