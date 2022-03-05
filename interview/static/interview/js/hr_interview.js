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

var currentQuestion = 1;
var questionCount = 0;
var questionSet = {};

function attemptSkill(event) {
    let skill = event.target.value;
    let charSkill = parseInt($(`#char-${skill}`).html());
    let intSkill = parseInt($(`#interw-${skill}`).html());
    console.log(`charSkill: ${charSkill}`);
    console.log(`intSkill: ${intSkill}`);

    let randomNumber = Math.floor(Math.random() * intSkill) + 1;

    console.log(`randomnumber: ${randomNumber}`);
    console.log("");

    if (randomNumber <= charSkill) {
        setImpress("+", 3);
        $(`#${skill}-btn`).addClass("btn-success");
    } else {
        $(`#${skill}-btn`).addClass("btn-danger");
    }

    $(`#${skill}-btn`).prop("disabled",true);
}

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

    if (answer == "wild") {
        
        if (calculateOutcome(4, 10)) {
            setImpress("+", 5);
        } else {
            setImpress("-", 5);
        }

    } else if (questionSet[questionCount].answer.length != 0) {
        
        let correctAnswer = questionSet[questionCount].answer;

        if (correctAnswer == answer) {
            setImpress("+", 3);
        } else {
            setImpress("-", 3);
        }

    } else {
        
        let charSkill = parseInt($(`#char-${answer}`).html());
        let intSkill = parseInt($(`#interw-${answer}`).html());
        console.log(`charSkill: ${charSkill}`);
        console.log(`intSkill: ${intSkill}`);

        if (calculateOutcome(charSkill, intSkill)) {
            setImpress("+", 3);
        } else {
            setImpress("-", 3);
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
        $("#impression").html(impress_nbr + integer);
        $("#impression").addClass("text-success").animate({fontSize: '2em', fontWeight: '900'}, "medium");
        setTimeout(() => { 
            $("#impression").animate({fontSize: '1.25em', fontWeight: '300'}, "medium").removeClass("text-success");
            }, 800);
    } else if (impress_nbr - integer < 0) {
        $("#impression").html("0");
        $("#impression").addClass("text-danger").animate({fontSize: '2em', fontWeight: '900'}, "medium");
        setTimeout(() => { 
            $("#impression").animate({fontSize: '1.25em', fontWeight: '300'}, "medium").removeClass("text-danger");
            }, 800);
    } else {
        $("#impression").html(impress_nbr - integer);
        $("#impression").addClass("text-danger").animate({fontSize: '2em', fontWeight: '900'}, "medium");
        setTimeout(() => { 
            $("#impression").animate({fontSize: '1.25em', fontWeight: '300'}, "medium").removeClass("text-danger");
            }, 800);
    }
}
  

function calculateOutcome(charSkill, intSkill) {
    let randomNumber = Math.floor(Math.random() * intSkill) + 1;
    console.log(`Randomnumber: ${randomNumber}`);
    console.log(`Randomnumber <= charSkill: ${randomNumber <= charSkill}`);

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
    setTimeout(() => { $("#question-game-area").addClass("hide"); }, 2000);

    if (finalScore >= neededScore) {
        setTimeout(() => { $("#ending-success").removeClass("hide"); }, 2000);
        setTimeout(() => { $("#ending-success").animate({opacity: 1}, "medium"); }, 2000);
    } else {
        setTimeout(() => { $("#ending-fail").removeClass("hide"); }, 2000);
        setTimeout(() => { $("#ending-fail").animate({opacity: 1}, "medium"); }, 2000);
    }
}
  