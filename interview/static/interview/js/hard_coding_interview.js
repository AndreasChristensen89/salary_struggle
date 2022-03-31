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
            $(".number-btn").click(passNumber);
            $("#submit-number-btn").click(passNumberAnswer);
            $(".code-btn").click(passCode);
            $("#submit-code-btn").click(passCodeAnswer);
            $("#answer-text").animate({fontWeight: '600'}, "medium");
            $("#answer-text").animate({fontWeight: '300'}, "medium");
            $("#answer-charm-btn").click(checkAnswer);
            $("#answer-intellect-btn").click(checkAnswer);
            $("#answer-coding-btn").click(checkAnswer);
            $("#question-text").animate({opacity: 1}, "medium");
            buildQuestions();
            timer();
        }
        });
});
var energy = parseInt($("#energy").text());
var currentQuestion = 1;
var questionCount = 0;
var questionSet = {};
var timeleft = 0;
var time = 8;
var finalScore = 1;
var neededScore = parseInt($("#interw-impress").text());

// Sends an ajax request to reset player's energy.
// Done in order to prevent players from reloading windom an resetting interview
// Energy is needed to start interview
// get the CSRF token
const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;
// remove the token from the DOM
document.querySelector('[name=csrfmiddlewaretoken]').remove();

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

// runs timer, calls next question if time out
function timer() {
    var timer = setInterval(function(){
        if(timeleft >= time){
            setImpress("-", 3);
            timeleft = 0;
            $("#answer-text").html("");
            $("#answer-code").html("");
            buildQuestions();
        } else if (currentQuestion > 9) {
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

// builds the next question
// changes setup at question 6, 10, finishes at 12
// at question 10 set timeleft to -1 to stop timer
function buildQuestions() {
    if (currentQuestion > 12) {
        $(".answer-btn").prop("disabled",true);
        finishInterview();
    } else if (currentQuestion > 9) {
        questionSet = hardCodingQuestions;
        $("#timer-row").addClass("hide");
        $(".answer-buttons").removeClass("hide");
        $("#code-buttons").addClass("hide");
        $("#question-text").text(questionSet[questionCount].question);
        $("#answer-charm").text(questionSet[questionCount].a);
        $("#answer-intellect").text(questionSet[questionCount].b);
        $("#answer-coding").text(questionSet[questionCount].c);
        $("#bubble-row").removeClass("hide");
        $("#bubble").removeClass("hide");
        setTimeout(() => {
            $("#question-text").animate({opacity: 1}, "slow");
            $("#skill-answers").animate({opacity: "1"}, 300);
        }, 500);
        questionCount++;
    } else if (currentQuestion < 6) {
        timeleft = 0;
        let randInt1 = Math.floor(Math.random() * 10) + 1;
        let randInt2 = Math.floor(Math.random() * 10) + 1;
        $("#question-text").html(`What is ${randInt1} * ${randInt2}`);
    } else if (currentQuestion > 5 ) {
        timeleft = 0;
        $("#number-buttons").addClass("hide");
        $("#code-buttons").removeClass("hide");
        let randCode = Math.floor(Math.random() * 20) + 5;
        $("#question-text").html(`Produce ${randCode}`);
        time = 12;
    }
}

// Checks if skill chosen is sufficient
// Compares to interviewers level
function checkAnswer(event) {
    $("#skill-answers").animate({opacity: "0"}, 300);
    let skill = event.target.value;

    $(".skill-btn").prop("disabled", true);

    $("#bubble").text($(`#answer-${skill}`).text());
    $("#bubble-row").removeClass("hide");
    $("#bubble").removeClass("hide");

    setTimeout(() => {
        $("#bubble").animate({
            opacity: 1
        }, "medium");
    }, 200);
    
    let charSkill = parseInt($(`#char-${skill}`).html());
    let intSkill = parseInt($(`#interw-${skill}`).html());

    let randomNumber = Math.floor(Math.random() * intSkill) + 1;

    setTimeout(() => {
        if (randomNumber <= charSkill) {
            setImpress("+", 3);
        } else {
            setImpress("-", 3);
        }
    }, 1000);

    setTimeout(() => {
        $("#bubble").animate({opacity: 0}, "medium");
        currentQuestion++;
        questionCount++;
        $("#question-text").animate({opacity: 0}, "medium");
    }, 2500);
    setTimeout(() => {
        if (questionCount == questionSet.length) {
            finishInterview();
        } else {
            timeleft = 0;
            buildQuestions();
            $(".skill-btn").prop("disabled", false);
        }
    }, 3500);

}

// animates and updates the impress integer
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
    currentQuestion++;
    $("#question").html(currentQuestion);
}

// Compares final score to needed score
// If enough then win screen and level up via ajax,
// otherwise fail screen
function finishInterview() {
    $("#question-game-area").animate({opacity: 0}, "slow");
    setTimeout(() => { $("#question-game-area").addClass("hide"); }, 1500);

    if (finalScore >= neededScore) {
        $.ajax({
            type: "POST",
            url: "/interview/interview-success/",
            headers: {'X-CSRFToken': csrf},
        });

        setTimeout(() => { $("#ending-success").removeClass("hide"); }, 1500);
        setTimeout(() => { $("#ending-success").animate({opacity: 1}, "medium"); }, 1500);
    } else {
        setTimeout(() => { $("#ending-fail").removeClass("hide"); }, 1500);
        setTimeout(() => { $("#ending-fail").animate({opacity: 1}, "medium"); }, 1500);
    }
}
  