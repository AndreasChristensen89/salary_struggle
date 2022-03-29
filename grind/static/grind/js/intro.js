document.addEventListener('DOMContentLoaded', function () {
    $('#next-btn').click(nextIntro);
    $("#intro-btn").click(function(){
        $("#intro-btn").animate({opacity: "0"}, "slow");
        setTimeout(() => {
            $("#intro-btn").addClass("hide");
            $('#intro-box').removeClass("hide");
            $('#next-intro').removeClass("hide").animate({opacity: "1.0"}, 1000);
            $('.intro-text').eq(0).removeClass("hide").animate({opacity: "1.0"}, 1000);
            $("#next-btn").removeClass("hide");
            setTimeout(() => {
                $("#skip-btn").removeClass("d-none");
                $("#next-btn").animate({opacity: "1.0"}, "slow");
                $("#skip-btn").animate({opacity: "1.0"}, "slow");
            }, 2000);
        }, 1000);
    });
});

var hint = 0;

function nextIntro() {
    $(".intro-text").eq(hint).animate({opacity: "0"}, "slow");
    setTimeout(() => {
        $(".intro-text").eq(hint).addClass("hide");
        $("#intro-btn").addClass("hide");
        hint++;
        $(".intro-text").eq(hint).removeClass("hide").animate({opacity: "1"}, "slow");
        if (hint == 12) {
                $('#next-btn').addClass("hide");
                $("#skip-btn").addClass("d-none");
            }
        }, 500);
}