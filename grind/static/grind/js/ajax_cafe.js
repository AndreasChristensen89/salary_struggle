// get the CSRF token
const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;
// remove the token from the DOM
document.querySelector('[name=csrfmiddlewaretoken]').remove();

var intellect = parseInt($("#intellect").text());
var energy = parseInt($("#energy").text());
var coding = parseInt($("#coding").text());
var endurance = parseInt($("#endurance").text());

$("#study").click(function() {
    let randomNumber = Math.floor(Math.random() * 3) + 1;
    console.log(randomNumber);
    console.log(randomNumber <= 2);
    
    $.ajax({
    type: "POST",
    url: "/grind/cafe-study/",
    headers: {'X-CSRFToken': csrf},
    data: {
        'random_number': randomNumber
    },
    success: function(){
        if (energy-(60-endurance) >= 0) {
            if (randomNumber <= 2) {
                $("#coding").text(coding+2);
                $("#intellect").text(intellect+2);
                codingLvl = $("#coding").text();
                intellectLvl = $("#intellect").text();
                $("#coding-win-increase").html(`Coding: ${codingLvl}`);
                $("#intellect-win-increase").html(`Intellect: ${intellectLvl}`);
                
                    
                intellect = intellect + 2;
                coding = coding + 2;
                
                $('.overview').fadeToggle(100);
                $(".loading-overlay").eq(0).fadeToggle(100);

            setTimeout(() => { 
                $('.overview').fadeToggle(100);
                $(".loading-overlay").eq(0).fadeToggle(100);
            }, 3000);
            } else {
                $("#intellect").text(intellect+1);
                $("#coding").text(coding+1);
                codingLvl = $("#coding").text();
                intellectLvl = $("#intellect").text();
                $("#coding-fail-increase").html(`Coding: ${codingLvl}`);
                $("#intellect-fail-increase").html(`Intellect: ${intellectLvl}`);
                    
                intellect = intellect + 1;
                coding = coding + 1;

                $('.overview').fadeToggle(100);
                $(".loading-overlay").eq(1).fadeToggle(100);

                setTimeout(() => { 
                    $('.overview').fadeToggle(100);
                    $(".loading-overlay").eq(1).fadeToggle(100);
                }, 3000);
            }
            $("#energy").html(`<i class="fas fa-bolt mx-1"></i> ${energy-(60-endurance)}`);
            energy = energy-(60-endurance);
        } else {
            $("#game-message").text(`You need ${60-endurance} energy`);
            $("#game-message-container").removeClass("d-none");

            setTimeout(() => { 
                $("#game-message-container").addClass("d-none");
            }, 1500);
        }   
    }
    }); 
});