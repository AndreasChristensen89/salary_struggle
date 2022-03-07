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
            buildQuestions();
        }
        });
});

var currentQuestion = 1;
var questionCount = 0;
var questionSet = {};

function attemptSkill(event) {
    let skill = event.target.value;
    let charSkill = parseInt($(`#char-${skill}`).html());
    let intSkill = parseInt($(`#interw-${skill}`).html());

    let randomNumber = Math.floor(Math.random() * intSkill) + 5;

    if (randomNumber <= charSkill) {
        setImpress("+", 3);
    } else {
        setImpress("-", 3);
    }

    buildQuestions();
}

function buildQuestions() {
    questionSet = codingQuestions;
    if (questionCount < questionSet.length) {
        $("#question-text").html(questionSet[questionCount].question);
        $("#answer1-btn").html(questionSet[questionCount].a);
        $("#answer2-btn").html(questionSet[questionCount].b);
        $("#answer3-btn").html(questionSet[questionCount].c);
    }
}

function checkAnswer(event) {
    let answer = event.target.value;
    let correctAnswer = questionSet[questionCount].answer;
    console.log(answer);
    console.log(correctAnswer);
    let impress = parseInt($("#impression").html());

    if (correctAnswer == answer) {
        setImpress("+", 3);
    } else if (impress - 3 >= 0) {
        setImpress("-", 3);
    } else {
        setImpress("-", 0)
    }

    if (questionCount == questionSet.length-1) {
        $(".answer-btn").prop("disabled",true);
        finishInterview();
    } else {
        buildQuestions();
    }
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
        $.ajax({
        type: "POST",
        url: "/grind/agency-skill/",
        headers: {'X-CSRFToken': csrf},
        data: {
            'random_number': randomNumber,
            'skill': skill
        },
        success: function(){
            if (parseInt($(`#${skill}`).text()) >= randomNumber && level == 1) {
                success();
            } else {
                fail(skill);
            }
        }
        });
        setTimeout(() => { $("#ending-success").removeClass("hide"); }, 1500);
        setTimeout(() => { $("#ending-success").animate({opacity: 1}, "medium"); }, 1500);
    } else {
        setTimeout(() => { $("#ending-fail").removeClass("hide"); }, 1500);
        setTimeout(() => { $("#ending-fail").animate({opacity: 1}, "medium"); }, 1500);
    }
}
  