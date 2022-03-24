// get the CSRF token
const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;
// remove the token from the DOM
document.querySelector('[name=csrfmiddlewaretoken]').remove();

var charm = parseInt($("#charm").text());
var intellect = parseInt($("#intellect").text());
var money = parseInt($("#money").text());
var energy = parseInt($("#energy").text());
var endurance = parseInt($("#endurance").text());
var coding = parseInt($("#coding").text());
var day = parseInt($("#day").text());

var energyPenalty = parseInt($("#energyPenalty").text())

$("#sleep").click(function() {
    $.ajax({
        type: "POST",
        url: "/grind/sleep/",
        headers: {'X-CSRFToken': csrf},
        success: function(){
            if (energy < 100) {
                $("#energy").html(`<i class="fas fa-bolt mx-1"></i> ${100-energyPenalty}`);
                $("#day").html(`<i class="far fa-calendar-alt"></i> ${day+1}`);

                // applying energy penalty, if any
                energy = 100-energyPenalty;
                day++;

                // resetting penalty
                energyPenalty = 0;

                $('.overview').fadeToggle(100);
                $(".loading-overlay").eq(0).fadeToggle(100);

                setTimeout(() => { 
                    $('.overview').fadeToggle(100);
                    $(".loading-overlay").eq(0).fadeToggle(100);
                }, 4000);
            } else {
                $("#game-message").text("Already full energy");
                $("#game-message-container").removeClass("d-none");

                setTimeout(() => { 
                    $("#game-message-container").addClass("d-none");
                }, 1500);
            }
            
        }
    });
});

$("#homeCharm").click(function() {
    $.ajax({
        type: "POST",
        url: "/grind/charm-home/",
        headers: {'X-CSRFToken': csrf},
        success: function(){
            if (energy - (40-endurance) >= 0 ) {
                $("#charm").text(charm+1);
                charm = charm+1;
                $("#energy").html(`<i class="fas fa-bolt mx-1"></i> ${energy-(40-endurance)}`);
                energy = energy-(40-endurance);

                $('.overview').fadeToggle(100);
                $(".loading-overlay").eq(2).fadeToggle(100);

                setTimeout(() => { 
                    $('.overview').fadeToggle(100);
                    $(".loading-overlay").eq(2).fadeToggle(100);
                }, 1500);
            } else {
                $("#game-message").text("Not enough energy");
                $("#game-message-container").removeClass("d-none");

                setTimeout(() => { 
                    $("#game-message-container").addClass("d-none");
                }, 1500);
            }
            
        }
    });
});


$("#homeStudy").click(function() {
    $.ajax({
        type: "POST",
        url: "/grind/study-home/",
        headers: {'X-CSRFToken': csrf},
        success: function(){
            if (energy - (40-endurance) >= 0 ) {
                $("#energy").html(`<i class="fas fa-bolt mx-1"></i> ${energy-(40-endurance)}`);
                $("#coding").text(coding+1);;

                coding = coding+1;
                energy = energy- (40-endurance);

                $('.overview').fadeToggle(100);
                $(".loading-overlay").eq(1).fadeToggle(100);

                setTimeout(() => { 
                    $('.overview').fadeToggle(100);
                    $(".loading-overlay").eq(1).fadeToggle(100);
                }, 1500);

            } else {
                $("#game-message").text("Not enough energy");
                $("#game-message-container").removeClass("d-none");

                setTimeout(() => { 
                    $("#game-message-container").addClass("d-none");
                }, 1500);
            }
            
        }
    });
});