// Adds eventlistener, adds function to hide intro by click

document.addEventListener('DOMContentLoaded', function () {

    $("#next-comment").click(function(){
        $(".intro").addClass("hide");
        $(".interviewer").removeClass("hide")
        });
    
});




  