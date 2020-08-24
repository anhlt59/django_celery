var host = "http://" + $(location).attr('host');

function get_users_count() {
    $.ajax({
        url: host + "/api/tasks/users-count",
        method: 'GET',
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
    }).done((res) => {
        // update task_status div
        $("#total").text(res.total);
        $("#superuser").text(res.superuser);
        $("#staffuser").text(res.staffuser);
        $("#users_update_time").text(res.update_time);
    })
}

function get_statistic_covid() {
    $.ajax({
        url: host + "/api/tasks/statistic-covid",
        method: 'GET',
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
    }).done((res) => {
        // update task_status div
        $("#covid_update_time").text(res.update_time);
        $("#covid_cases").text(res.total);
        $("#covid_deaths").text(res.deaths);
        $("#covid_recovered").text(res.recovered);

    })
}

$(document).ready(function () {
    get_users_count();
    get_statistic_covid();


    setTimeout(function () {
        get_users_count();
        get_statistic_covid();
    }, 5000);

})
