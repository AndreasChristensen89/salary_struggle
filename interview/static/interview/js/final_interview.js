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
            $(".number-btn").click(passNumber);
            $("#submit-number-btn").click(passNumberAnswer);
            $(".code-btn").click(passCode);
            $("#submit-code-btn").click(passCodeAnswer);
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
var timeleft = 0;
var time = 8;

// checks the answer if answer is a skill
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
        $("#question-text").animate({
            opacity: 0
        }, "medium");
    }, 2500);

    setTimeout(() => {
        buildQuestions();
    }, 3500);
}

function timer() {
    var timer = setInterval(function(){
        if(timeleft >= time){
            setImpress("-", 3);
            timeleft = 0;
            $("#answer-text").html("");
            $("#answer-code").html("");
            buildQuestions();
        } else if (currentQuestion == 21) {
            clearInterval(timer);
        }

        $("#timer").html(time - timeleft);
        timeleft++;
    }, 1000);
}

// copies value of number-buttons to text, or deletes last char if delete
function passCode(event) {
    let selectedAction = event.target.value;
    let length = $("#answer-code").html().length;

    if (selectedAction === "delete") {
        if (length > 0) {
            $("#answer-code").html($("#answer-code").html().slice(0, -1));
        }
    } else {
            $("#answer-code").html($("#answer-code").html() + selectedAction);
        }
}

// gets the number from the button-value
// adds the number to the text, replacing the intro text
// if delete is passed deletes last char if length > 0
function passNumber(event) {
    let selectedAction = event.target.value;
    let length = $("#answer-text").html().length;

    if ($("#answer-text").html() == "Hurry! Use the buttons!") {
        $("#answer-text").html(selectedAction);
    } else if (selectedAction === "delete") {
        if (length > 0) {
        $("#answer-text").html($("#answer-text").html().slice(0, -1));
        }
    } else {
        $("#answer-text").html($("#answer-text").html() + selectedAction);
    }
}

// calculates if answer in text matches multiplication-answer
function passNumberAnswer() {
    let int1 = $("#question-text").html().slice(8, 9);
    let int2 = $("#question-text").html().slice(12);
    let rightAnswer = int1 * int2;

    if ($("#answer-text").text() == rightAnswer) {
        setImpress("+", 3);
    } else {
        setImpress("-", 3);
    }
    $("#answer-text").html("");
    buildQuestions();
}

// Checks if answer is correct, calls StringCalculator
// Checks for illegal characters in first and last char
// Checks for double operator symbols
function passCodeAnswer() {
    let str = $("#answer-code").html();
    let firstChar = $("#answer-code").html().slice(0, 1);
    let lastChar = $("#answer-code").html().slice(-1);
    let button = $("#submit-code-btn");
    let correctAnswer = $("#question-text").html().slice(-2);
    
    if (firstChar == "*" || firstChar == "+" || firstChar == "-") {
        button.addClass("bg-danger");
        setTimeout(() => { button.removeClass("bg-danger"); }, 1000);
    } else if (lastChar == "*" || lastChar == "+" || lastChar == "-") {
        button.addClass("bg-danger");
        setTimeout(() => { button.removeClass("bg-danger"); }, 1000);
    } else if (str.includes("--") || str.includes("++") || str.includes("**")) {
        button.addClass("bg-danger");
        setTimeout(() => { button.removeClass("bg-danger"); }, 1000);
    } else {        
        if (stringCalculator(str) == correctAnswer.trim()) {
            setImpress("+", 3);
        } else {
        setImpress("-", 3);
        }
    $("#answer-code").html("");
    buildQuestions();
      }
}

// calculates the math in a string
function stringCalculator(fn) {
    return new Function('return ' + fn)();
}


function buildQuestions() {
    if (questionCount == 20) {
        finishInterview();
    }
    
    // updates html question number
    $("#question").html(currentQuestion);
    questionSet = finalInterviewQuestions;
    currentQuestion++;
    questionCount++;

    if (currentQuestion < 7) {
        // if there's an answer we hide skills and reveal questions
        if (questionSet[questionCount].answer.length != 0) {
            $("#skill-answers").addClass("hide");
            $("#bubble-row").addClass("hide");
            $("#question-answers").removeClass("hide");
        }
        
        $("#question-text").text(questionSet[questionCount].question);
        $("#question-text").animate({opacity: 1}, "slow");
        $("#answer-intellect").text(questionSet[questionCount].a);
        $("#answer-charm").text(questionSet[questionCount].b);
        $("#answer-coding").text(questionSet[questionCount].c);
        $("#answer-wild").text(questionSet[questionCount].d);
        $("#question-text").animate({opacity: 1}, "slow");
        $(".skill-btn").prop("disabled", false);
        setTimeout(() => {
            $(".answer-btn").animate({opacity: 1}, "slow");
            $("#skill-answers").animate({opacity: "1"}, 300);
        }, 500);
    } else if (currentQuestion <= 14) {
        timeleft = 0;
        $("#bubble-row").addClass("hide");
        $("#math-section").removeClass("hide");
        $("#question-answers").addClass("hide");
        $("#timer-row").removeClass("hide");
        // start timer only at first question
        if (currentQuestion == 7) {
            setTimeout(() => {
                timer();
            }, 1500);
        }
        $("#question-text").animate({opacity: 1}, "slow");
        let randInt1 = Math.floor(Math.random() * 10) + 1;
        let randInt2 = Math.floor(Math.random() * 10) + 1;
        $("#question-text").html(`What is ${randInt1} * ${randInt2}`);
    } else if (currentQuestion <= 20) {
        timeleft = 0;
        time = 12;
        $("#number-buttons").addClass("hide");
        $("#code-buttons").removeClass("hide");
        let randCode = Math.floor(Math.random() * 20) + 5;
        $("#question-text").html(`Produce ${randCode}`);
    }
}

// checks the answer if not skill
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
    else if (answer == "wild") {
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
        $("#question-text").animate({opacity: 0}, "medium");
        $(".answer-btn").animate({opacity: 0}, "medium");
    }, 1500);
    setTimeout(() => {
        buildQuestions();
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