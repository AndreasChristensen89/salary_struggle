// get the CSRF token
const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;
// remove the token from the DOM
document.querySelector('[name=csrfmiddlewaretoken]').remove();

var intellect = parseInt($("#intellect").text());
var energy = parseInt($("#energy").text());
var energyPenalty = parseInt($("#energyPenalty").text());
var coding = parseInt($("#coding").text());
var endurance = parseInt($("#endurance").text());
var money = parseInt($("#money").text());

$("#fight").click(function() {
    let randomNumber = Math.floor(Math.random() * 10) + 1;
    console.log(randomNumber);
    
    $.ajax({
    type: "POST",
    url: "/grind/fight/",
    headers: {'X-CSRFToken': csrf},
    data: {
        'random_number': randomNumber
    },
    success: function(){
        if (energyPenalty < 50) {
            if (energy-60 >= 0) {
                if (endurance <= 21) {
                    if (randomNumber >= 5) {
                        $("#endurance").text(endurance + 3);
                        $("#energy").html(`<i class="fas fa-bolt mx-1"></i> ${energy-(60-endurance)}`);
                            
                        endurance = endurance + 3;
                        energy = energy-(60-endurance);

                        $('.overview').fadeToggle(100);
                        $(".loading-overlay").eq(0).fadeToggle(100);

                        setTimeout(() => { 
                            $('.overview').fadeToggle(100);
                            $(".loading-overlay").eq(0).fadeToggle(100);
                        }, 3000);
                    } else {
                        $("#energy").html(`<i class="fas fa-bolt mx-1"></i> 0`); 
                        energy = 0;

                        $('.overview').fadeToggle(100);
                        $(".loading-overlay").eq(1).fadeToggle(100);

                        setTimeout(() => { 
                            $('.overview').fadeToggle(100);
                            $(".loading-overlay").eq(1).fadeToggle(100);
                        }, 3000);
                    }
                } else {
                    $("#game-message").text("You're too strong. Noone wants to fight you.");
                    $("#game-message-container").removeClass("d-none");

                    setTimeout(() => { 
                        $("#game-message-container").addClass("d-none");
                    }, 1500);
                }
            } else {
                $("#game-message").text("Your body is too messed up to fight");
                $("#game-message-container").removeClass("d-none");

                setTimeout(() => { 
                    $("#game-message-container").addClass("d-none");
                }, 1500);
            }
        } else {
            $("#game-message").text("Your body is too messed up to fight");
            $("#game-message-container").removeClass("d-none");

            setTimeout(() => { 
                $("#game-message-container").addClass("d-none");
            }, 1500);
        }   
    }
    }); 
});

$("#gamble").click(function() {
    let randomNumber = Math.floor(Math.random() * 3) + 1;
    
    $.ajax({
    type: "POST",
    url: "/grind/gamble/",
    headers: {'X-CSRFToken': csrf},
    data: {
        'random_number': randomNumber
    },
    success: function(){
        if (money >= 1000) {
            if (randomNumber == 1) {
                $("#money").html(`<i class="fas fa-yen-sign ml-1"></i> ${money + 1500}`);      
                money = money + 1500

                $('.overview').fadeToggle(100);
                $(".loading-overlay").eq(2).fadeToggle(100);

                setTimeout(() => { 
                    $('.overview').fadeToggle(100);
                    $(".loading-overlay").eq(2).fadeToggle(100);
                }, 3000);
            } else {
                $("#money").html(`<i class="fas fa-yen-sign ml-1"></i> ${money - 1000}`); 
                money = money - 1000

                $('.overview').fadeToggle(100);
                $(".loading-overlay").eq(3).fadeToggle(100);

                setTimeout(() => { 
                    $('.overview').fadeToggle(100);
                    $(".loading-overlay").eq(3).fadeToggle(100);
                }, 3000);
            }
        } else {
            $("#game-message").text("You're too poor. Get a job.");
            $("#game-message-container").removeClass("d-none");

            setTimeout(() => { 
                $("#game-message-container").addClass("d-none");
            }, 1500);
        }
    }
    }); 
});