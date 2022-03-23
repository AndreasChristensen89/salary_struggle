var hint = 0;

document.addEventListener('DOMContentLoaded', function () {
    $('#next-hint').click(nextHint);
    $("#hint-btn").click(function(){
            // $('#hint-text').removeClass("hide");
            $("#introHrInterview").removeClass("d-none");
            $('#bubble-agency').css('opacity', '1');
            $('#bubble-agency').text($(".hint").eq(hint).text());
            $("#hint-row").addClass("d-none");
            $('#next-hint').removeClass("d-none");
            // $('.hint').eq(0).removeClass("hide").animate({opacity: "1.0"}, 1000);
            $("#next-hint").delay(2000).animate({opacity: "1.0"}, "fast");
        });
});

function nextHint() {
    hint++;
    $('#bubble-agency').text($(".hint").eq(hint).text());

    if ($(".hint").eq(hint).length) {
    } else {
        $('#next-hint').addClass("d-none");
        // $('#hint-text').addClass("d-none");
        // $("#hint-row").removeClass("d-none");
        $("#introHrInterview").addClass("d-none");
        $('#hrInterviewLink').removeClass("d-none");
        hint = 0;
    }
}