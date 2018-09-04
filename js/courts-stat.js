/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

$(document).ready(function () {
    $('#current-selection').html('Статистика');
    fetchStat();
});

function fetchStat() {
    $.ajax({
        url: '/wsgi-bin/fetchcourtsstat',
        processData: false,
        contentType: false,
        type: 'GET',
        success: function (data) {
            fillStat(data);
        }
    });
}

function fillStat(data) {
    var json = JSON.parse(data).data;

    var tree = [
        {
            text: "Районные суды",
            selectable: false,
            nodes: [
                {
                    text: "Некоторые показатели",
                    selectable: false,
                    nodes: [
                        {
                            text: 'АДМ',
                            selectable: false,
                            nodes: []
                        },
                        {
                            text: 'ГР',
                            selectable: false,
                            nodes: []
                        },
                        {
                            text: 'УГ',
                            selectable: false,
                            nodes: []
                        }
                    ]
                }
            ]
        },
        {
            text: "Мировые суды",
            selectable: false,
            nodes: [
                {
                    text: "Нагрузка",
                    selectable: false,
                    nodes: []
                }
            ]
        }
    ];

    for (var j of json) {
        var node = null;
        switch (j.stat_type) {
            case 'RAI_SUMMARY_ADM':
                node = tree[0].nodes[0].nodes[0].nodes;
                break;
            case 'RAI_SUMMARY_CIV':
                node = tree[0].nodes[0].nodes[1].nodes;
                break;
            case 'RAI_SUMMARY_CRIM':
                node = tree[0].nodes[0].nodes[2].nodes;
                break;
            case 'MIR_CHARGE':
                node = tree[1].nodes[0].nodes;
                break;
        }
        for (var d of j.stat_data) {
            node.push({text: `${d.year} (${d.mod} квартал)`, href: d.data});
        }
    }

    $('#tree').treeview({
        data: tree,
        showTags: true,
        enableLinks: false,
        levels: 5
    });
}

$(document).on('nodeSelected', '#tree', function (event, data) {
    $('.details').attr('data', 'resource/pdf/' + data.href);
    var parent = $('#tree').treeview('getParent', data.nodeId);
    var root = $('#tree').treeview('getParent', parent.nodeId);
    while (root.parentId !== undefined) {
        root = $('#tree').treeview('getParent', root.nodeId);
    }
    $('#current-selection').html(root.text + ' | ' + parent.text + ' | ' + data.text);
});
