const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;
document.querySelector('[name=csrfmiddlewaretoken]').remove();

var charm = parseInt($("#charm").text());
var energy = parseInt($("#energy").text());
var endurance = parseInt($("#endurance").text());
var money = parseInt($("#money").text());

// apply for a job ajax
$("#apply").click(function() {
    let randomNumber = Math.floor(Math.random() * 20) + 1;
    console.log(randomNumber);
    console.log(charm >= randomNumber);
    
    $.ajax({
    type: "POST",
    url: "/grind/apply-job/",
    headers: {'X-CSRFToken': csrf},
    success: function(){
        if (energy >= (60-endurance)) {
            if (charm >= 20) {
                $("#passed").removeClass("hide");

                $('.overview').fadeToggle(100);
                $(".loading-overlay").eq(0).fadeToggle(100);

                setTimeout(() => { 
                    $('.overview').fadeToggle(100);
                    $(".loading-overlay").eq(0).fadeToggle(100);
                }, 5000);
            } else {
                $("#rejected").removeClass("hide");
                
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

// work ajax
$("#work").click(function() {
    let salary = charm * 100;
    
    $.ajax({
    type: "POST",
    url: "/grind/work/",
    headers: {'X-CSRFToken': csrf},
    success: function(){
        if (energy >= (60-endurance)) {
            $("#money").html(`<i class="fas fa-yen-sign ml-1"></i> ${money + salary}`);
            $("#energy").html(`<i class="fas fa-bolt mx-1"></i> ${energy-(60-endurance)}`);

            money = money + salary;
            energy = energy - (60 - endurance);

            $('.overview').fadeToggle(100);
            $(".loading-overlay").eq(0).fadeToggle(100);

            setTimeout(() => { 
                $('.overview').fadeToggle(100);
                $(".loading-overlay").eq(0).fadeToggle(100);
            }, 3000);
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