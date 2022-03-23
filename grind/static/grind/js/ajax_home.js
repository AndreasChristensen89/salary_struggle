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
                $("#homeCharm").addClass("bg-danger");
                setTimeout(() => { 
                    $("#homeCharm").removeClass("bg-danger");
                }, 800);
            }
            
        }
    });
});

var energyPenalty = parseInt($("#energyPenalty").text())
var charmPenalty = parseInt($("#charmPenalty").text())
var codingPenalty = parseInt($("#codingPenalty").text())
var intellectPenalty = parseInt($("#intellectPenalty").text())
var endurancePenalty = parseInt($("#endurancePenalty").text())

$("#sleep").click(function() {
    $.ajax({
        type: "POST",
        url: "/grind/sleep/",
        headers: {'X-CSRFToken': csrf},
        success: function(){
            if (energy < 100) {
                $("#charm").text(charm+-charmPenalty);
                $("#energy").html(`<i class="fas fa-bolt mx-1"></i> ${100-energyPenalty}`);
                $("#intellect").text(intellect-intellectPenalty);
                $("#coding").text(coding-codingPenalty);
                $("#endurance").text(endurance-endurancePenalty);
                $("#day").html(`<i class="far fa-calendar-alt"></i> ${day+1}`);

                // applying penalties, if any
                coding = coding-codingPenalty;
                intellect = intellect-intellectPenalty;
                energy = 100-energyPenalty;
                charm = charm-charmPenalty;
                endurance = endurance-endurancePenalty;
                day++;

                // resetting penalties, in case user stays and performs new actions
                codingPenalty = 0;
                intellectPenalty = 0;
                energyPenalty = 0;
                charmPenalty = 0;
                endurancePenalty = 0;

                $('.overview').fadeToggle(100);
                $(".loading-overlay").eq(0).fadeToggle(100);

                setTimeout(() => { 
                    $('.overview').fadeToggle(100);
                    $(".loading-overlay").eq(0).fadeToggle(100);
                }, 3000);
            } else {
                $("#sleep").addClass("bg-danger");
                setTimeout(() => { 
                    $("#sleep").removeClass("bg-danger");
                }, 800);
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
                $("#homeStudy").addClass("bg-danger");
                setTimeout(() => { 
                    $("#homeStudy").removeClass("bg-danger");
                }, 800);
            }
            
        }
    });
});