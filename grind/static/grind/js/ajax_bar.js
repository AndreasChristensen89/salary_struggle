const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;

document.querySelector('[name=csrfmiddlewaretoken]').remove();

var charm = parseInt($("#charm").text());
var money = parseInt($("#money").text());
var energy = parseInt($("#energy").text());
var endurance = parseInt($("#endurance").text());

// posts and ajax call to the BarDrink class
// updates variables, calls first instance of class overlay if money
$("#drinkButton").click(function() {
    $.ajax({
        type: "POST",
        url: "/grind/bar-drink/",
        headers: {'X-CSRFToken': csrf},
        success: function(){
            if (energy >= (40-endurance)) {
                if (money >= 1000) {
                    $("#charm").text(charm+2);
                    charmLvl = $("#charm").text();
                    $("#money").html(`<i class="fas fa-yen-sign ml-1"></i> ${money-1000}`);
                    
                    $("#charm-increase").text(`Charm level: ${charmLvl}`)

                    $('.overview').fadeToggle(100);
                    $(".loading-overlay").eq(0).fadeToggle(100);

                    money = money-1000;
                    charm = charm+2;

                    setTimeout(() => { 
                        $('.overview').fadeToggle(100);
                        $(".loading-overlay").eq(0).fadeToggle(100);
                    }, 3000);
                } else {
                    $("#game-message").text('You need 1000 <i class="fas fa-yen-sign ml-1"></i>');
                    $("#game-message-container").removeClass("d-none");

                    setTimeout(() => { 
                        $("#game-message-container").addClass("d-none");
                    }, 1500);
                }
                $("#energy").html(`<i class="fas fa-bolt mx-1"></i> ${energy-(40-endurance)}`);
                energy = energy-(40-endurance);
            } else {
                $("#game-message").text(`You need ${40-endurance} energy`);
                $("#game-message-container").removeClass("d-none");

                setTimeout(() => { 
                    $("#game-message-container").addClass("d-none");
                }, 1500);
            }
        }
    });
});

$("#converse").click(function() {
    let randomNumber = Math.floor(Math.random() * 3) + 1;
    console.log(randomNumber);
    console.log(randomNumber <= 2);
    
    $.ajax({
    type: "POST",
    url: "/grind/bar-converse/",
    headers: {'X-CSRFToken': csrf},
    data: {
        'random_number': randomNumber
    },
    success: function(){
        if (energy >= (40-endurance)) {
            if (randomNumber <= 2) {
                $("#charm").text(charm+2);
                charmLvl = $("#charm").text();
                $("#charm-increase").text(`Charm level: ${charmLvl}`)

                charm = charm+2;

                $('.overview').fadeToggle(100);
                $(".loading-overlay").eq(0).fadeToggle(100);
                $('#drink-pen').addClass('d-none');

                setTimeout(() => { 
                    $('.overview').fadeToggle(100);
                    $(".loading-overlay").eq(0).fadeToggle(100);
                }, 2500);
                setTimeout(() => {
                    $('#drink-pen').removeClass('d-none');
                }, 2700);
            } else {
                $('.overview').fadeToggle(100);
                $(".loading-overlay").eq(1).fadeToggle(100);
    
                setTimeout(() => { 
                    $('.overview').fadeToggle(100);
                    $(".loading-overlay").eq(1).fadeToggle(100);
                }, 2500);
            }
            $("#energy").html(`<i class="fas fa-bolt mx-1"></i> ${energy-(40-endurance)}`);
            energy = energy-(40-endurance);
        } else {
            $("#game-message").text(`You need ${40-endurance} energy`);
            $("#game-message-container").removeClass("d-none");

            setTimeout(() => { 
                $("#game-message-container").addClass("d-none");
            }, 1500);
        }
        
            
    }
    }); 
});