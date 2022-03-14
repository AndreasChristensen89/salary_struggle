document.addEventListener('DOMContentLoaded', function () {
    $('#next-hint').click(nextHint);
    $("#hint-btn").click(function(){
            $('#hint-text').removeClass("hide");
            $('#next-hint').removeClass("hide");
            $("#hint-row").addClass("hide");
            $(".hint").addClass("temp");
            $('.hint').eq(0).removeClass("hide").animate({opacity: "1.0"}, 1000);
            $("#next-hint").delay(2000).animate({opacity: "1.0"}, "fast");
        });
});

var hint = 0;

function nextHint() {
    $(".temp").eq(hint).addClass("hide");
    hint++;

    if ($(".temp").eq(hint).length) {
        $(".temp").eq(hint).removeClass("hide");
    } else {
        $('#next-hint').addClass("hide");
        $('#hint-text').addClass("hide");
        $(".temp").removeClass("temp");
        $("#hint-row").removeClass("hide");
        $("#HRInterview").removeClass("hide");
        hint = 0;
    }
}