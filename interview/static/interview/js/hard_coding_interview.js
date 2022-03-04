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
            $(".number-btn").click(passNumber);
            $("#submit-number-btn").click(passNumberAnswer);
            $("#answer-text").animate({fontWeight: '900'}, "medium");
            $("#answer-text").animate({fontWeight: '300'}, "medium");
            buildQuestions();
            timer();
        }
        });
});
var currentQuestion = 1;
var questionCount = 0;
var questionSet = {};
var timeleft = 0;


function passCode(event) {
    let selectedAction = event.target.value;
    let length = $("#answer-code").html().length;

    if (selectedAction === "delete") {
        if (length > 7) {
            $("#answer-code").html($("#answer-code").html().slice(0, -1));
        }
    } else {
            $("#answer-code").html($("#answer-code").html() + selectedAction);
        }
}

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

function passNumberAnswer() {
    let int1 = $("#question-text").html().slice(8, 9);
    let int2 = $("#question-text").html().slice(12);
    let rightAnswer = int1 * int2;

    if ($("#answer-text").html() == rightAnswer) {
        setImpress("+", 3);
    } else {
        setImpress("-", 3);
    }
    $("#answer-text").html("");
    buildQuestions();
}


function passCodeAnswer() {
    let int1 = $("#answer-code").html().slice(7);
    let firstChar = $("#answer-code").html().slice(7, 8);
    let lastChar = $("#answer-code").html().slice(-1);
    let button = $("#submit-code-btn");
    let correctAnswer = $("#question-text").html().slice(-2);
    
    if (firstChar == "*" || firstChar == "+" || firstChar == "-") {
        button.addClass("bg-danger");
        setTimeout(() => { button.removeClass("bg-danger"); }, 1000);
    } else if (lastChar == "*" || lastChar == "+" || lastChar == "-") {
        button.addClass("bg-danger");
        setTimeout(() => { button.removeClass("bg-danger"); }, 1000);
    } else if (int1.includes("--") || int1.includes("++") || int1.includes("**")) {
        button.addClass("bg-danger");
        setTimeout(() => { button.removeClass("bg-danger"); }, 1000);
    } else {
        console.log(stringCalculator(int1));
        console.log(correctAnswer.trim());
        console.log(stringCalculator(int1) == correctAnswer.trim());
        
        if (stringCalculator(int1) == correctAnswer.trim()) {
            setImpress("+", 3);
        } else {
        setImpress("-", 3);
        }
    $("#answer-code").html("return ");
    buildQuestions();
      }
}

// calculates the math in a string
function stringCalculator(fn) {
    return new Function('return ' + fn)();
}


function timer() {
    
    setInterval(function(){
        if(timeleft >= 100){
            setImpress("-", 3);
            timeleft = 0;
            buildQuestions();
        }
        $("#timer").html(100 - timeleft);
        timeleft++;
    }, 1000);
}


function attemptSkill(event) {
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

function buildQuestions() {
    if (currentQuestion >= 6) {
        timeleft = 0;
        $("#number-buttons").addClass("hide");
        $("#code-buttons").removeClass("hide");
        // checks if one button has events, and if so we can assume that submit is similar
        let events = $._data(document.getElementById('codeplus-btn'), "events");
        let hasEvents = (events != null);
        if (hasEvents == false) {
            $(".code-btn").click(passCode);
            $("#submit-code-btn").click(passCodeAnswer);
        }
        let randCode = Math.floor(Math.random() * 12) + 1;
        $("#question-text").html(`Create a return statement that produces ${randCode}`);
    } else if (currentQuestion < 6) {
        timeleft = 0;
        let randInt1 = Math.floor(Math.random() * 10) + 1;
        let randInt2 = Math.floor(Math.random() * 10) + 1;
        $("#question-text").html(`What is ${randInt1} * ${randInt2}`);
    }

    if (currentQuestion == 20) {
        $(".answer-btn").prop("disabled",true);
        finishInterview();
    }
}

function checkAnswer(event) {
    let answer = event.target.value;
    let correctAnswer = questionSet[questionCount].answer;
    let impress = parseInt($("#impression").html());

    if (correctAnswer == answer) {
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
    questionCount++;
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
  