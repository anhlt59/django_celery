// custom javascript
var host = "http://" + $(location).attr('host');

$('.button').on('click', function () {
    if (!$(this).attr('sleep_time')) return null;
    if (!$("#task_result_table .table100").length) {
        var html = `
        <h2 class="title">Task Result</h2>
        <div class="table100 ver5 m-b-110">
            <div class="table100-head">
                <table>
                    <thead>
                        <tr class="row100 head">
                            <th class="cell100 column1">ID</th>
                            <th class="cell100 column2">Status</th>
                            <th class="cell100 column3">Result</th>
                            <th class="cell100 column4">Time</th>
                        </tr>
                    </thead>
                </table>
            </div>

            <div class="table100-body js-pscroll">
                <table>
                    <tbody id="tasks">
                    </tbody>
                </table>
            </div>
        </div>
        `
        $('#task_result_table').prepend(html);
    }
    let params = {sleep_time: $(this).attr('sleep_time')};

    if ($(this).hasClass("celery")) {
        let url = host + '/api/tasks/celery';
        $.ajax({
            url: url,
            data: params,
            method: 'POST',
        }).done((res) => {
            getStatus(res.task_id);
        }).fail((err) => {
            alert(err);
        });
    } else {
        let url = host + '/api/tasks/nomal';
        $.ajax({
            url: url,
            data: params,
            method: 'POST',
        }).done((res) => {
            // append to task_status div
            var html = `
                <tr class="row100 body">
                    <td class="cell100 column1"></td>
                    <td class="cell100 column2">${res.status}</td>
                    <td class="cell100 column3">${res.result}</td>
                    <td class="cell100 column4">${res.date_done}</td>
                </tr>`
            $('#tasks').prepend(html);
        }).fail((err) => {
            alert(err);
        });
    }
});

function getStatus(taskID) {
    if (!taskID) return null;
    let params = {task_id: taskID};
    $.ajax({
        url: host + "/api/tasks/celery",
        method: 'GET',
        dataType: 'json',
        data: params,
        contentType: 'application/json; charset=utf-8',
    }).done((res) => {
            if ($(`#${res.task_id}`).length) {
                // update task_status div
                $(`#${res.task_id}_status`).text(res.status);
                $(`#${res.task_id}_result`).text(res.result);
                $(`#${res.task_id}_date_done`).text(res.date_done);
            } else {
                // append to task_status div
                var html = `
                <tr class="row100 body" id="${res.task_id}">
                    <td class="cell100 column1">${res.task_id}</td>
<!--                    <td class="cell100 column2">...</td>-->
                    <td class="cell100 column2" id="${res.task_id}_status">${res.status}</td>
                    <td class="cell100 column3" id="${res.task_id}_result"></td>
                    <td class="cell100 column4" id="${res.task_id}_date_done"></td>
                </tr>`
                $('#tasks').prepend(html);
            }
            // reload
            var taskStatus = res.status;
            if (taskStatus !== 'SUCCESS' && taskStatus !== 'FAILURE') {
                setTimeout(function () {
                    getStatus(res.task_id);
                }, 1000);
            }
        }
    ).fail((err) => {
        alert(err)
    });
}

(function ($) {
    "use strict";
    $('.column100').on('mouseover', function () {
        var table1 = $(this).parent().parent().parent();
        var table2 = $(this).parent().parent();
        var verTable = $(table1).data('vertable') + "";
        var column = $(this).data('column') + "";

        $(table2).find("." + column).addClass('hov-column-' + verTable);
        $(table1).find(".row100.head ." + column).addClass('hov-column-head-' + verTable);
    });

    $('.column100').on('mouseout', function () {
        var table1 = $(this).parent().parent().parent();
        var table2 = $(this).parent().parent();
        var verTable = $(table1).data('vertable') + "";
        var column = $(this).data('column') + "";

        $(table2).find("." + column).removeClass('hov-column-' + verTable);
        $(table1).find(".row100.head ." + column).removeClass('hov-column-head-' + verTable);
    });

})(jQuery);
