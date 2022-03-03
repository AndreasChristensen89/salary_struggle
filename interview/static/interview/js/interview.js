// Adds eventlistener, adds function to hide intro by click
document.addEventListener('DOMContentLoaded', function () {
    $(".intro").animate({opacity: "1.0"}, "slow")

    $("#next-comment").click(function(){
        if (!$(".intro").hasClass("hide")) {
            $(".intro").animate({opacity: "0"}, "slow");
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
            $(".chance-btn").click(attemptSkill);
            $("#answer1-btn").click(checkAnswer);
            $("#answer2-btn").click(checkAnswer);
            $("#answer3-btn").click(checkAnswer);
            $("#answer4-btn").click(checkAnswer);
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
    if (questionCount < questionSet.length) {
        $("#question-text").html(questionSet[questionCount].question);
        $("#answer1-btn").html(questionSet[questionCount].a);
        $("#answer2-btn").html(questionSet[questionCount].b);
        $("#answer3-btn").html(questionSet[questionCount].c);
        $("#answer4-btn").html(questionSet[questionCount].d);
    }
}

function checkAnswer(event) {
    let answer = event.target.value;
    let impress = parseInt($("#impression").html());

    if (questionSet[questionCount].answer.length != 0) {
        let correctAnswer = questionSet[questionCount].answer;

        if (correctAnswer == answer) {
            setImpress("+", 3);
        } else if (impress - 3 > 0) {
                setImpress("-", 3);
        } else {
            $("#impression").text("0");
        }
    } else if (answer != "wild") {
        let charSkill = parseInt($(`#char-${answer}`).html());
        let intSkill = parseInt($(`#interw-${answer}`).html());

        if (calculateOutcome(charSkill, intSkill)) {
            setImpress("+", 3);
        } else if (impress-3 > 0) {
            setImpress("-", 3);
        } else {
            $("#impression").html("0");
        }
    } else {
        if (calculateOutcome(4, 10)) {
            setImpress("+", 5);
        } else if (impress-5 > 0) {
            setImpress("-", 5);
        } else {
            $("#impression").html("0");
        }
    }
    if (questionCount == questionSet.length-1) {
        $(".answer-btn").prop("disabled",true);
        finishInterview();
    } else {
        currentQuestion++;
        questionCount++;
        $("#question").html(currentQuestion);
        buildQuestions();
    }
}

function setImpress(plusMinus, integer) {
    let impress_nbr = parseInt($("#impression").html());
    if (plusMinus == "+") {
        $("#impression").text(impress_nbr + integer);
    } else {
        $("#impression").text(impress_nbr - integer);
    }
    $("#impression").animate({fontSize: '2em', fontWeight: '900', color: '"#fff"'}, "medium");
    $("#impression").animate({fontSize: '1.25em', fontWeight: '300', color: 'black'}, "medium");
}
  

function calculateOutcome(charSkill, intSkill) {
    let randomNumber = Math.floor(Math.random() * (intSkill - 1 + 1) + 1);

    if (randomNumber <= charSkill) {
        return true;
    } else {
        return false;
    }
}

function finishInterview() {
    let finalScore = parseInt($("#impression").html());
    let neededScore = parseInt($("#impress-level").html());
    $("#question-game-area").animate({opacity: 0}, "slow");
    setTimeout(() => { $("#question-game-area").addClass("hide"); }, 1500);

    if (finalScore >= neededScore) {
        setTimeout(() => { $("#ending-success").removeClass("hide"); }, 1500);
        setTimeout(() => { $("#ending-success").animate({opacity: 1}, "medium"); }, 1500);
    } else {
        setTimeout(() => { $("#ending-fail").removeClass("hide"); }, 1500);
        setTimeout(() => { $("#ending-fail").animate({opacity: 1}, "medium"); }, 1500);
    }
}
  