const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;

document.querySelector('[name=csrfmiddlewaretoken]').remove();

var charm = parseInt($("#charm").text());
var money = parseInt($("#money").text());
var energy = parseInt($("#energy").text());
var endurance = parseInt($("#endurance").text());

$("#drinkButton").click(function() {
    $.ajax({
        type: "POST",
        url: "/grind/bar-drink/",
        headers: {'X-CSRFToken': csrf},
        success: function(){
            if (energy >= (40-endurance)) {
                if (money >= 1000) {
                    $("#charm").text(charm+2);
                    $("#money").html(`<i class="fas fa-yen-sign ml-1"></i> ${money-1000}`);
                    charm = charm+2;
                    money = money-1000;

                    $('.overview').fadeToggle(100);
                    $(".loading-overlay").eq(0).fadeToggle(100);

                    setTimeout(() => { 
                        $('.overview').fadeToggle(100);
                        $(".loading-overlay").eq(0).fadeToggle(100);
                    }, 3000);
                } else {
                    $("#drinkButton").addClass("bg-danger");
                    setTimeout(() => { 
                        $("#drinkButton").removeClass("bg-danger");
                    }, 800);
                }
                $("#energy").html(`<i class="fas fa-bolt mx-1"></i> ${energy-(40-endurance)}`);
                energy = energy-(40-endurance);
            } else {
                $("#drinkButton").addClass("bg-danger");
                setTimeout(() => { 
                    $("#drinkButton").removeClass("bg-danger");
                }, 800);
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
        if (energy >= (40-endurance) && randomNumber <= 2) {
            $("#converse").addClass("bg-success");
            $("#charm").text(charm+2);
            $("#energy").html(`<i class="fas fa-bolt mx-1"></i> ${energy-(40-endurance)}`);
                
            charm = charm+2;
            energy = energy-(40-endurance);

            setTimeout(() => { 
                $("#converse").removeClass("bg-success");
            }, 800);
        } else {
            $("#converse").addClass("bg-danger");
            $("#energy").text(energy-(40-endurance));
            energy = energy-(40-endurance);
            setTimeout(() => { 
                $("#converse").removeClass("bg-danger");
            }, 800);
        }
            
    }
    }); 
});