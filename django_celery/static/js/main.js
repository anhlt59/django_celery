// custom javascript

$('.button').on('click', function () {
    $.ajax({
        url: 'api/tasks',
        data: {type: $(this).data('sleep_time')},
        method: 'POST',
    })
        .done((res) => {
            getStatus(res.task_id);
        })
        .fail((err) => {
            alert(err);
        });
});

function getStatus(taskID, retries = 4) {
    var params = {task_id: taskID}
    console.log(params);

    $.ajax({
        url: `api/tasks`,
        method: 'GET',
        dataType: 'json',
        data: params,
        contentType: 'application/json; charset=utf-8',
    })
        .done((res) => {
            if ($(`#${res.task_id}`)) {
                var html = `
                    <tr class="row100 body">
                        <td class="cell100 column1">${res.task_id}</td>
                        <td class="cell100 column2">...</td>
                        <td class="cell100 column3" id="${res.task_id}_status">${res.status}</td>
                        <td class="cell100 column4" id="${res.task_id}_result">${res.result}</td>
                        <td class="cell100 column5" id="${res.task_id}_date_done">${res.date_done}</td>
                    </tr>`
                $('#tasks').prepend(html);
            } else {
                var html = `
                    <tr class="row100 body">
                        <td class="cell100 column1">${res.task_id}</td>
                        <td class="cell100 column2">...</td>
                        <td class="cell100 column3" id="${res.task_id}_status">${res.status}</td>
                        <td class="cell100 column4" id="${res.task_id}_result">${res.result}</td>
                        <td class="cell100 column5" id="${res.task_id}_date_done">${res.date_done}</td>
                    </tr>`
                $('#tasks').prepend(html);
            }
            // var taskStatus = res.task_status;
            // if (retries && (taskStatus === 'SUCCESS' || taskStatus === 'FAILURE')) return false;
            // setTimeout(function () {
            //     getStatus(res.task_id, retries - 1);
            // }, 1000);
        }
)
  .fail((err) => {
    alert(err)
  });
}

(function ($) {
	"use strict";
	$('.column100').on('mouseover',function(){
		var table1 = $(this).parent().parent().parent();
		var table2 = $(this).parent().parent();
		var verTable = $(table1).data('vertable')+"";
		var column = $(this).data('column') + "";

		$(table2).find("."+column).addClass('hov-column-'+ verTable);
		$(table1).find(".row100.head ."+column).addClass('hov-column-head-'+ verTable);
	});

	$('.column100').on('mouseout',function(){
		var table1 = $(this).parent().parent().parent();
		var table2 = $(this).parent().parent();
		var verTable = $(table1).data('vertable')+"";
		var column = $(this).data('column') + "";

		$(table2).find("."+column).removeClass('hov-column-'+ verTable);
		$(table1).find(".row100.head ."+column).removeClass('hov-column-head-'+ verTable);
	});

})(jQuery);
