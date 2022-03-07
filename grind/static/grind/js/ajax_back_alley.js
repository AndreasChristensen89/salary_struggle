// get the CSRF token
const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;
// remove the token from the DOM
document.querySelector('[name=csrfmiddlewaretoken]').remove();

var intellect = parseInt($("#intellect").text());
var energy = parseInt($("#energy").text());
var coding = parseInt($("#coding").text());
var endurance = parseInt($("#endurance").text());
var money = parseInt($("#money").text());

$("#fight").click(function() {
    let randomNumber = Math.floor(Math.random() * 10) + 1;
    
    $.ajax({
    type: "POST",
    url: "/grind/fight/",
    headers: {'X-CSRFToken': csrf},
    data: {
        'random_number': randomNumber
    },
    success: function(){
        if (energy-(60-endurance) >= 0) {
            if (randomNumber >= 5) {
                $("#fight").addClass("bg-success");
                $("#endurance").text(endurance + 3);
                $("#energy").text(energy-(60-endurance));
                    
                endurance = endurance + 3;
                energy = energy-(60-endurance);

                setTimeout(() => { 
                    $("#fight").removeClass("bg-success");
                }, 800);
            } else {
                $("#fight").addClass("bg-warning");
                $("#energy").text(0);
                    
                energy = 0;

                setTimeout(() => { 
                    $("#fight").removeClass("bg-warning");
                }, 800);
            }
        } else {
            $("#fight").addClass("bg-danger");
            setTimeout(() => { 
                $("#fight").removeClass("bg-danger");
            }, 800);
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
        if (randomNumber == 1) {
            $("#gamble").addClass("bg-success");
            $("#money").text(money + 2000);
                    
            money = money + 2000

            setTimeout(() => { 
                $("#gamble").removeClass("bg-success");
            }, 800);
        } else {
            $("#gamble").addClass("bg-warning");
            $("#money").text(money - 1000);
                    
            money = money - 1000

            setTimeout(() => { 
                $("#gamble").removeClass("bg-warning");
            }, 800);
            }
        }
    }); 
});