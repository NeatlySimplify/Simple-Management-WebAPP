$(document).ready(function () {
    $('.app-route').click(function (e) { 
        e.preventDefault();
        const route = $(this).attr('href');
        $.ajax({
            type: "GET",
            url: route,
            dataType: "html",
            success: function (response) {
                $('#main_content').html(response);
            },
        });
    });
});