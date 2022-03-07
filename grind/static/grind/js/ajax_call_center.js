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
    data: {
        'random_number': randomNumber
    },
    success: function(){
        if (energy >= (60-endurance)) {
            if (charm >= randomNumber) {
                $("#energy").text(energy - (60-endurance));
                $('.overview').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                $("#apply").addClass("hide");
                $("#passed").removeClass("hide");

                setTimeout(() => {
                    $('.overview').fadeToggle(100);
                    $('#loading-overlay').fadeToggle(100);
                }, 1500);
            } else {
                $("#energy").text(energy - (60-endurance));
                $("#apply").addClass("bg-danger");

                setTimeout(() => {
                    $("#apply").addClass("hide");
                    $("#rejected").removeClass("hide");
                }, 1000);
                
            }
        } else {
            $("#apply").addClass("bg-danger");
            setTimeout(() => {
                $("#apply").removeClass("bg-danger");
            }, 800);
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
            $("#work").addClass("bg-success");
            $("#money").text(money + salary);
            $("#energy").text(energy - (60 - endurance));

            money = money + salary;
            energy = energy - (60 - endurance);

            setTimeout(() => {
                $("#work").removeClass("bg-success");
            }, 800);
        } else {
            $("#work").addClass("bg-danger");
            setTimeout(() => { 
                $("#work").removeClass("bg-danger");
            }, 800);
        }   
    }
    }); 
});