// Adds eventlistener, adds function to hide intro by click
document.addEventListener('DOMContentLoaded', function () {
    
    $(".intro").animate({opacity: "1.0"}, "slow");

    $("#next-comment").click(function(){
        if (!$(".intro").hasClass("hide")) {
            $(".intro").animate({opacity: "0"}, "slow");
            $(".intro").addClass("hide");
            $('.intro-interviewer').removeClass("hide");
            $(".intro-interviewer").animate({opacity: "1.0"}, "slow");
            $('#interviewer').removeClass("hide");
            $("#interviewer").animate({opacity: "1.0"}, "slow");
        }
        else if (!$(".intro-interviewer").hasClass("hide")) {
            $(".intro-interviewer").addClass("hide");
            $("#head-intro").addClass("hide");
            $(".interviewer-presentation").removeClass("hide");
        } else {

            $("#introduction").addClass("hide");
            $("#next-button").addClass("hide");
            $("#question-game-area").removeClass("hide");
            $(".skill-btn").click(attemptSkill);
            $(".answer-btn").click(checkAnswer);
            buildQuestions();

        }
    });
});

// get the CSRF token
const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;
// remove the token from the DOM
document.querySelector('[name=csrfmiddlewaretoken]').remove();

var energy = parseInt($("#energy").text());
$.ajax({
    type: "POST",
    url: "/interview/reset-energy/",
    headers: {
        'X-CSRFToken': csrf
    },
    success: function () {
        $("#energy").html(`<i class="fas fa-bolt mx-1"></i> 0`);
        energy = 0;
    }
});

var currentQuestion = 1;
var questionCount = 0;
var questionSet = {};
var finalScore = 1;
var neededScore = parseInt($("#interw-impress").text());

// checks the answer if answer is a skill
function attemptSkill(event) {
    $("#question-answers").animate({opacity: "0"}, 300);
    $("#skill-answers").animate({opacity: "0"}, 300);
    // get the skill
    let skill = event.target.value;
    // disable answer buttons
    $(".skill-btn").prop("disabled", true);
    $(".answer-btn").prop("disabled", true);
    // hide answers choices
    $("#question-answers").animate({opacity: "0"}, 500);
    setTimeout(() => {
        $("#question-answers").addClass("hide");
    }, 500);
    
    // set bubble text to answer and display it
    setTimeout(() => {
        $("#bubble").text($(`#answer-${skill}`).text());
        $("#bubble-row").removeClass("hide");
        $("#bubble").removeClass("hide");
    }, 500);

    // else get char and interviewer's skill level
    let charSkill = parseInt($(`#char-${skill}`).html());
    let intSkill = parseInt($(`#interw-${skill}`).html());

    // generate random number
    let randomNumber = Math.floor(Math.random() * intSkill) + 1;

    setTimeout(() => {
        $("#bubble").animate({
            opacity: 1
        }, "medium");
    }, 500);

    setTimeout(() => {
        if (randomNumber <= charSkill) {
            setImpress("+", 3);
        } else {
            setImpress("-", 3);
        }
    }, 2000);

    setTimeout(() => {
        $("#bubble").animate({
            opacity: 0
        }, "medium");
        currentQuestion++;
        questionCount++;
        $("#question-text").animate({
            opacity: 0
        }, "medium");
    }, 4000);
    setTimeout(() => {
        if (questionCount == questionSet.length) {
            finishInterview();
        } else {
            buildQuestions();
            $(".skill-btn").prop("disabled", false);
            $(".answer-btn").prop("disabled", false);
            $("#question-answers").animate({opacity: "1"}, 300);
            $("#skill-answers").animate({opacity: "1"}, 300);
        }
    }, 5000);
}

function buildQuestions() {
    $("#question").html(currentQuestion);
    questionSet = codingQuestions;
    // extract next question
    $("#question-text").html(questionSet[questionCount].question);
    $("#bubble-row").addClass("hide");
    $("#question-answers").removeClass("hide");

    $("#question-text").html(questionSet[questionCount].question);
    $("#answer-a").html(questionSet[questionCount].a);
    $("#answer-b").html(questionSet[questionCount].b);
    $("#answer-c").html(questionSet[questionCount].c);
    $("#answer-charm").html(questionSet[questionCount].charm);
    $("#answer-intellect").html(questionSet[questionCount].intellect);
    $("#answer-coding").html(questionSet[questionCount].coding);
    $("#question-text").animate({opacity: 1}, "slow");
    $("#question-answers").animate({opacity: "1"}, 500);
    setTimeout(() => {
        $(".answer-btn").animate({opacity: 1}, "slow");
    }, 500);
}

// checks the answer is not skill
function checkAnswer(event) {
    $("#skill-answers").animate({opacity: "0"}, 300);
    $(".skill-btn").prop("disabled", true);
    $(".answer-btn").prop("disabled", true);
    
    let answer = event.target.value;
        
    let correctAnswer = questionSet[questionCount].answer;

    if (correctAnswer == answer) {
        $(event.target).addClass("bg-success");
        setImpress("+", 3);
        setTimeout(() => {
            $(event.target).removeClass("bg-success");
        }, 1000);
    } else {
        setImpress("-", 3);
        $(event.target).addClass("bg-danger");
        setTimeout(() => {
            $(event.target).removeClass("bg-danger");
        }, 1000);
    }

    setTimeout(() => {
        currentQuestion++;
        questionCount++;
        $("#question-text").animate({opacity: 0}, "medium");
        $(".answer-btn").animate({opacity: 0}, "medium");
    }, 1500);
    setTimeout(() => {
        if (questionCount == questionSet.length) {
            finishInterview();
        } else {
            buildQuestions();
            $(".skill-btn").prop("disabled", false);
            $(".answer-btn").prop("disabled", false);
            $("#skill-answers").animate({opacity: "1"}, 300);
        }
    }, 2500);
}

function setImpress(plusMinus, integer) {
    
    let impress_nbr = parseInt($("#impression").html());
    if (plusMinus == "+") {
        finalScore += integer;
        $("#impression").html(impress_nbr + integer);
        $("#impression").addClass("text-success").animate({fontSize: '2em', fontWeight: '900'}, "medium");
        setTimeout(() => { 
            $("#impression").animate({fontSize: '1.25em', fontWeight: '300'}, "medium").removeClass("text-success");
            }, 800);
    } else if (impress_nbr - integer < 0) {
        finalScore = 0;
        $("#impression").html("0");
        $("#impression").addClass("text-danger").animate({fontSize: '2em', fontWeight: '900'}, "medium");
        setTimeout(() => { 
            $("#impression").animate({fontSize: '1.25em', fontWeight: '300'}, "medium").removeClass("text-danger");
            }, 800);
    } else {
        finalScore -= integer;
        $("#impression").html(impress_nbr - integer);
        $("#impression").addClass("text-danger").animate({fontSize: '2em', fontWeight: '900'}, "medium");
        setTimeout(() => { 
            $("#impression").animate({fontSize: '1.25em', fontWeight: '300'}, "medium").removeClass("text-danger");
        }, 800);
    }
}
  

function calculateOutcome(charSkill, intSkill) {
    let randomNumber = Math.floor(Math.random() * intSkill) + 1;

    if (randomNumber <= charSkill) {
        return true;
    } else {
        return false;
    }
}

function finishInterview() {
    $("#question-game-area").animate({opacity: 0}, "slow");
    setTimeout(() => { $("#question-game-area").addClass("hide"); }, 2000);

    if (finalScore >= neededScore) {
        $.ajax({
            type: "POST",
            url: "/interview/interview-success/",
            headers: {'X-CSRFToken': csrf},
        });
        setTimeout(() => { $("#ending-success").removeClass("hide"); }, 2000);
        setTimeout(() => { $("#ending-success").animate({opacity: 1}, "medium"); }, 2000);
    } else {
        setTimeout(() => { $("#ending-fail").removeClass("hide"); }, 2000);
        setTimeout(() => { $("#ending-fail").animate({opacity: 1}, "medium"); }, 2000);
    }
}