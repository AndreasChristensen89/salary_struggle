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

// Sends an ajax request to reset player's energy.
// Done in order to prevent players from reloading windom an resetting interview
// Energy is needed to start interview

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

function attemptSkill(event) {
    $("#skill-answers").animate({opacity: "0"}, 300);
    // get the skill
    let skill = event.target.value;
    // disable answer buttons
    $(".skill-btn").prop("disabled", true);
    // set bubble text to answer and display it
    $("#bubble").text($(`#answer-${skill}`).text());
    $("#bubble").removeClass("hide");

    // 40% chance of winning if "wild" is chosen
    if (skill == "wild") {
        setTimeout(() => {
            $("#bubble").animate({
                opacity: 1
            }, "medium");
        }, 200);

        setTimeout(() => {
            if (calculateOutcome(4, 10)) {
                setImpress("+", 5);
            } else {
                setImpress("-", 5);
            }
        }, 1000);
    } else {
        // else get char and interviewer's skill level
        let charSkill = parseInt($(`#char-${skill}`).html());
        let intSkill = parseInt($(`#interw-${skill}`).html());

        // generate random number
        let randomNumber = Math.floor(Math.random() * intSkill) + 1;

        setTimeout(() => {
            $("#bubble").animate({
                opacity: 1
            }, "medium");
        }, 200);

        setTimeout(() => {
            if (randomNumber <= charSkill) {
                setImpress("+", 3);
            } else {
                setImpress("-", 3);
            }
        }, 1000);
    }

    setTimeout(() => {
        $("#bubble").animate({
            opacity: 0
        }, "medium");
        currentQuestion++;
        questionCount++;
        $("#question-text").animate({
            opacity: 0
        }, "medium");
    }, 2500);
    setTimeout(() => {
        if (questionCount == questionSet.length) {
            finishInterview();
        } else {
            buildQuestions();
            $(".skill-btn").prop("disabled", false);
            $("#skill-answers").animate({opacity: "1"}, 300);
        }
    }, 3500);
}

function buildQuestions() {
    $("#question").html(currentQuestion);
    questionSet = hrQuestions;
    if (questionSet[questionCount].answer.length != 0) {
        if (questionCount < questionSet.length) {
            $("#skill-answers").addClass("hide");
            $("#bubble-row").addClass("hide");
            $("#question-answers").removeClass("hide");
        }
    } else {
        $("#question-text").html(questionSet[questionCount].question);
    }
    $("#question-text").html(questionSet[questionCount].question);
    $("#answer-intellect").html(questionSet[questionCount].a);
    $("#answer-charm").html(questionSet[questionCount].b);
    $("#answer-coding").html(questionSet[questionCount].c);
    $("#answer-wild").html(questionSet[questionCount].d);
    $("#question-text").animate({opacity: 1}, "slow");
    setTimeout(() => {
        $(".answer-btn").animate({opacity: 1}, "slow");
    }, 500);
}

function checkAnswer(event) {

    let answer = event.target.value;
        
    let correctAnswer = questionSet[questionCount].answer;

    if (correctAnswer == answer) {
        $(event.target).addClass("bg-success");
        setImpress("+", 3);
        setTimeout(() => {
            $(event.target).removeClass("bg-success");
        }, 1000);
    } 
    else if (answer == "wild") 
    {
        if (calculateOutcome(4, 10)) {
            $("#answer-wild").addClass("bg-success");
            setImpress("+", 5);
            setTimeout(() => {
                $("#answer-wild").removeClass("bg-success");
            }, 1000);
        } else {
            setImpress("-", 5);
            $("#answer-wild").addClass("bg-danger");
            setTimeout(() => {
                $("#answer-wild").removeClass("bg-danger");
            }, 1000);
        }
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
  