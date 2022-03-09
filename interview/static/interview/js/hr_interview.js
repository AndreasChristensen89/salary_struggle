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
            $(".skill-btn").click(attemptSkill);
            $(".answer-btn").click(checkAnswer);
            buildQuestions();
        }
        });
});

var currentQuestion = 1;
var questionCount = 0;
var questionSet = {};

function attemptSkill(event) {
    // get the skill
    let skill = event.target.value;
    // disable answer buttons
    $(".skill-btn").prop("disabled", true);
    // set bubble text to answer and display it
    $("#bubble").text($(`#answer-${skill}`).text())
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
        console.log(`Character ${skill} level: ${charSkill}`);
        console.log(`Interviewer ${skill} level ${intSkill}`);

        // generate random number
        let randomNumber = Math.floor(Math.random() * intSkill) + 1;

        console.log(`random number: ${randomNumber}`);
        console.log("");

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
        console.log(questionCount);
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
    console.log(answer);
        
    let correctAnswer = questionSet[questionCount].answer;
    console.log(correctAnswer);

    if (correctAnswer == answer) {
        $(event.target).addClass("bg-success")
        setImpress("+", 3);
        setTimeout(() => {
            $(event.target).removeClass("bg-success")
        }, 1000);
    } 
    else if (answer == "wild") 
    {
        if (calculateOutcome(4, 10)) {
            $("#answer-wild").addClass("bg-success")
            setImpress("+", 5);
            setTimeout(() => {
                $("#answer-wild").removeClass("bg-success")
            }, 1000);
        } else {
            setImpress("-", 5);
            $("#answer-wild").addClass("bg-danger")
            setTimeout(() => {
                $("#answer-wild").removeClass("bg-danger")
            }, 1000);
        }
    } else {
        setImpress("-", 3);
        $(event.target).addClass("bg-danger")
        setTimeout(() => {
            $(event.target).removeClass("bg-danger")
        }, 1000);
    }

    setTimeout(() => {
        currentQuestion++;
        questionCount++;
        console.log(questionCount);
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
    console.log(`Randomnumber <= 4: ${randomNumber <= 4}`);

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
  