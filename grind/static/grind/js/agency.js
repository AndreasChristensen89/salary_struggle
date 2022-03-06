
$("#hint-btn").click(function(){
            $('#hint-text').removeClass("hide");
            $('#next-hint').removeClass("hide");
            $(".hint").addClass("temp");
            $('#next-hint').click(nextHint);
            $('.hint').eq(0).removeClass("hide").animate({opacity: "1.0"}, 1000);
            $("#next-hint").delay(2000).animate({opacity: "1.0"}, "fast");
        });

var hint = 0;

function nextHint() {
    $(".temp").eq(hint).addClass("hide");
    hint++;

    if ($(".temp").eq(hint).length) {
        $(".temp").eq(hint).removeClass("hide").animate({opacity: "1.0"}, 300);
    } else {
        $('#next-hint').animate({opacity: "0.0"}, 500).addClass("hide");
    }
    
}