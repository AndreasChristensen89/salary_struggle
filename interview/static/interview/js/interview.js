// Adds eventlistener, adds function to hide intro by click

document.addEventListener('DOMContentLoaded', function () {

    $("#next-comment").click(function(){
        if (!$(".intro").hasClass("hide")) {
            $(".intro").addClass("hide");
            $('.intro-interviewer').removeClass("hide");
            $('#interviewer').removeClass("hide");
        }
        else if (!$(".intro-interviewer").hasClass("hide")) {
            $(".intro-interviewer").addClass("hide");
            $("#head-intro").addClass("hide");
            $(".interviewer-presentation").removeClass("hide");
        } else {
            $("#introduction").addClass("hide");
            $("#next-button").addClass("hide");
            $("#question-game-area").removeClass("hide");
            $(".chance-btn").click(attemptSkill)
        }
        });
});

function attemptSkill(event) {
    let skill = event.target.value;

    let charCharm = parseInt($("#char-charm").html());
    let charIntellect = parseInt($("#char-intellect").html());
    let charCoding = parseInt($("#char-coding").html());

    let intColdness = parseInt($("#interw-coldness").html());
    let intIntellect = parseInt($("#interw-intellect").html());
    let intCoding = parseInt($("#interw-coding").html());

    console.log(charCharm>intColdness)
    console.log(charIntellect>intIntellect)
    console.log(charCoding>intCoding)
    console.log(skill)
}





  