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
            $(".answer-btn").click(passNumber);
            $("#submit-btn").click(passAnswer);
            buildQuestions();
            timer();
        }
        });
});
var currentQuestion = 1;
var questionCount = 0;
var questionSet = {};
var timeleft = 0;

function passNumber(event) {
    let selectedAction = event.target.value;
    let length = $("#answer-text").html().length;

    if ($("#answer-text").html() == "Use buttons") {
        $("#answer-text").html(selectedAction);
    } else if (selectedAction === "delete") {
        if (length > 0) {
        $("#answer-text").html($("#answer-text").html().slice(0, -1));
        }
    } else {
        $("#answer-text").html($("#answer-text").html() + selectedAction);
    }
}

function passAnswer() {
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

function timer() {
    
    setInterval(function(){
        if(timeleft >= 5){
            setImpress("-", 3);
            timeleft = 0;
            buildQuestions();
        }
        $("#timer").html(5 - timeleft);
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
    questionSet = codingQuestions;
    if (questionCount == questionSet.length-1) {
        $(".answer-btn").prop("disabled",true);
        finishInterview();
    }

    if (questionCount < questionSet.length) {
        timeleft = 0;
        let randInt1 = Math.floor(Math.random() * 10) + 1;
        let randInt2 = Math.floor(Math.random() * 10) + 1;
        $("#question-text").html(`What is ${randInt1} * ${randInt2}`);
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
  