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
            buildQuestions();
        }
        });
});

// var timeLeft = 5;
// var timerId = setInterval(countdown, 1000);
var currentQuestion = 1;
var questionCount = 0;
var questionSet = {};

function attemptSkill(event) {
    let skill = event.target.value;
    let charSkill = parseInt($(`#char-${skill}`).html());
    let intSkill = parseInt($(`#interw-${skill}`).html());

    let randomNumber = Math.floor(Math.random() * (intSkill - 1 + 1) + 1);

    if (randomNumber <= charSkill) {
        let impress = parseInt($("#impression").text());
        $("#impression").text(impress+3);
        $("#impression").animate({fontSize: '2em', fontWeight: '900', color: '"#fff"'}, "medium");
        $("#impression").animate({fontSize: '1.25em', fontWeight: '300', color: 'black'}, "medium");
    }

    $(`#${skill}-btn`).prop("disabled",true);
}

// function countdown() {
//     if (timeLeft == -1) {
//         failContinue();
//     } else {
//         $('#timer').html(timeLeft);
//         timeLeft--;
//     }
// }

// function failContinue() {
//     $("#question").html(currentQuestion+1);
//     currentQuestion++;
//     console.log($("#question").html())
//     timeLeft = 5;
//     countdown();
// }

function buildQuestions() {
    questionSet = hrQuestions;
        $("#question-text").html(questionSet[questionCount].question);
        $("#answer1-btn").html(questionSet[questionCount].a).click(checkAnswer);
        $("#answer2-btn").html(questionSet[questionCount].b).click(checkAnswer);
        $("#answer3-btn").html(questionSet[questionCount].c).click(checkAnswer);
        $("#answer4-btn").html(questionSet[questionCount].d).click(checkAnswer);
}

function checkAnswer(event) {
    let answer = event.target.value;

    let charSkill = parseInt($(`#char-${answer}`).html());
    let intSkill = parseInt($(`#interw-${answer}`).html());

     if (calculateOutcome(charSkill, intSkill)) {
        currentQuestion++;
        $("#question").html(currentQuestion);
     } else {
        $("#question").html(currentQuestion);
     }
}
  

function calculateOutcome(charSkill, intSkill) {
    let randomNumber = Math.floor(Math.random() * (intSkill - 1 + 1) + 1);

    if (randomNumber <= charSkill) {
        let impress = parseInt($("#impression").text());
        $("#impression").text(impress+3);
        $("#impression").animate({fontSize: '2em', fontWeight: '900', color: '"#fff"'}, "medium");
        $("#impression").animate({fontSize: '1.25em', fontWeight: '300', color: 'black'}, "medium");
        return true;
    } else {
        return false;
    }
}



  