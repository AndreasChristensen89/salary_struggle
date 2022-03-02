// Adds eventlistener, adds function to hide intro by click

document.addEventListener('DOMContentLoaded', function () {
    $(".intro").animate({opacity: "1.0"}, "slow")

    $("#next-comment").click(function(){
        if (!$(".intro").hasClass("hide")) {
            $(".intro").animate({opacity: "0"}, "slow")
            $(".intro").addClass("hide");
            $('.intro-interviewer').removeClass("hide");
            $(".intro-interviewer").animate({opacity: "1.0"}, "slow")
            $('#interviewer').removeClass("hide");
            $("#interviewer").animate({opacity: "1.0"}, "slow")
        }
        else if (!$(".intro-interviewer").hasClass("hide")) {
            $(".intro-interviewer").addClass("hide");
            $("#head-intro").addClass("hide");
            $(".interviewer-presentation").removeClass("hide");
        } else {
            $("#introduction").addClass("hide");
            $("#next-button").addClass("hide");
            $("#question-game-area").removeClass("hide");
            $(".chance-btn").click(attemptSkill)
            countdown()
        }
        });
});

function attemptSkill(event) {
    let skill = event.target.value;
    let charSkill = parseInt($(`#char-${skill}`).html());
    let intSkill = parseInt($(`#interw-${skill}`).html());

    let randomNumber = Math.floor(Math.random() * (intSkill - 1 + 1) + 1);

    if (randomNumber <= charSkill) {
        let impress = parseInt($("#impression").text());
        $("#impression").text(impress+3);
        $("#impression").animate({fontSize: '2em', fontWeight: '900', color: '"#fff"'}, "medium");
        $("#impression").animate({fontSize: '1.25em', fontWeight: '300'}, "medium");
    }

    $(`#${skill}-btn`).prop("disabled",true);
}

var timeLeft = 2;
var timerId = setInterval(countdown, 1000);
var question = $("#question");

function countdown() {
    if (timeLeft == -1) {
        clearTimeout(timerId);
        doSomething();
    } else {
        $('#timer').html(timeLeft);
        timeLeft--;
    }
}

function doSomething() {
    question.html( "<strong>" + (parseInt ( $("#question").text() ) + 1) + "</strong>" );
}
  





  