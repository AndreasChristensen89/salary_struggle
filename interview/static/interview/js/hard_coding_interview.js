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
            // $(".chance-btn").click(attemptSkill);
            $(".number-btn").click(passNumber);
            $("#submit-number-btn").click(passNumberAnswer);
            $(".code-btn").click(passCode);
            $("#submit-code-btn").click(passCodeAnswer);
            $("#answer-text").animate({fontWeight: '900'}, "medium");
            $("#answer-text").animate({fontWeight: '300'}, "medium");
            $("#answer-charm-btn").click(checkAnswer);
            $("#answer-intellect-btn").click(checkAnswer);
            $("#answer-coding-btn").click(checkAnswer);
            $("#question-text").animate({opacity: 1}, "medium");
            buildQuestions();
            timer();

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
                headers: {'X-CSRFToken': csrf},
                success: function(){
                    $("#energy").html(`<i class="fas fa-bolt mx-1"></i> 0`);
                    energy = 0;
                    } 
            });
        }
        });
});
var currentQuestion = 1;
var questionCount = 0;
var questionSet = {};
var timeleft = 0;
var time = 8;


// copies value of number-buttons, or deletes last char if delete
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
    console.log(rightAnswer);
    console.log($("#answer-text").html());

    if ($("#answer-text").text() == rightAnswer) {
        setImpress("+", 3);
    } else {
        setImpress("-", 3);
    }
    $("#answer-text").html("");
    buildQuestions();
}

// checks for illegal characters in first and last char
// checks for double operator symbols
// uses stringCalculator to calculate text as math
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
        console.log(stringCalculator(str));
        console.log(correctAnswer.trim());
        console.log(stringCalculator(str) == correctAnswer.trim());
        
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

// runs timer, calls next question if time out
function timer() {
    setInterval(function(){
        if(timeleft >= time){
            setImpress("-", 3);
            timeleft = 0;
            $("#answer-text").html("");
            $("#answer-code").html("");
            buildQuestions();
        }
        $("#timer").html(time - timeleft);
        timeleft++;
    }, 1000);
}

// tests if chosen skill is sufficient
// resets timer and next question
function attemptSkill(event) {
    // get the skill
    let skill = event.target.value;
    // disable answer buttons
    $(".skill-btn").prop("disabled", true);

    $("#bubble").text($(`#answer-${skill}`).text())
    $("#bubble").removeClass("hide");

    let charSkill = parseInt($(`#char-${skill}`).html());
    let intSkill = parseInt($(`#interw-${skill}`).html());

    let randomNumber = Math.floor(Math.random() * intSkill) + 1;

    if (randomNumber <= charSkill) {
        setImpress("+", 3);
    } else {
        setImpress("-", 3);
    }
    timeleft = 0;
    buildQuestions();
}

// builds the next question
// changes setup at question 6, 10, finishes at 12
// at question 10 set timeleft to -1 to stop timer
function buildQuestions() {
    if (currentQuestion > 12) {
        $(".answer-btn").prop("disabled",true);
        finishInterview();
    } else if (currentQuestion > 9) {
        time = -1;
        questionSet = hardCodingQuestions;
        console.log(questionCount);
        $("#timer-row").addClass("hide");
        $(".answer-buttons").removeClass("hide");
        $("#code-buttons").addClass("hide");
        $("#question-text").text(questionSet[questionCount].question);
        $("#answer-intellect").text(questionSet[questionCount].a);
        $("#answer-charm").text(questionSet[questionCount].b);
        $("#answer-coding").text(questionSet[questionCount].c);
        $("#bubble-row").removeClass("hide");
        $("#bubble").removeClass("hide");
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
        $("#question-text").html(`Create a statement that results in ${randCode}`);
        time = 12;
    }

    if (currentQuestion == 20) {
        $(".answer-btn").prop("disabled",true);
        finishInterview();
    }
}

// double function
function checkAnswer(event) {
    let skill = event.target.value;
    let charSkill = parseInt($(`#char-${skill}`).html());
    let intSkill = parseInt($(`#interw-${skill}`).html());

    let randomNumber = Math.floor(Math.random() * intSkill) + 1;

    if (randomNumber <= charSkill) {
        setImpress("+", 3);
    } else {
        setImpress("-", 3);
    }

    timeleft = 0;
    buildQuestions();
}

function setImpress(plusMinus, integer) {
    let impress_nbr = parseInt($("#impression").html());
    if (plusMinus == "+") {
        $("#impression").html(impress_nbr + integer);
    } else if (impress_nbr - integer >= 0) {
        $("#impression").html(impress_nbr - integer);
    } else {
        $("#impression").html("0");
    }
    $("#impression").animate({fontSize: '2em', fontWeight: '900', color: '"#fff"'}, "medium");
    $("#impression").animate({fontSize: '1.25em', fontWeight: '300', color: 'black'}, "medium");
    currentQuestion++;
    $("#question").html(currentQuestion);
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
  