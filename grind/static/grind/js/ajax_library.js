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
    url: "/grind/library-study/",
    headers: {'X-CSRFToken': csrf},
    data: {
        'random_number': randomNumber
    },
    success: function(){
        if (energy-(60-endurance) >= 0) {
            if (randomNumber <= 2) {
                $("#study").addClass("bg-success");
                $("#intellect").text(intellect + 2);
                $("#coding").text(coding + 2);
                $("#energy").text(energy-(60-endurance));
                    
                intellect = intellect + 2;
                coding = coding + 2;
                energy = energy-(60-endurance);

                setTimeout(() => { 
                    $("#study").removeClass("bg-success");
                }, 800);
            } else {
                $("#study").addClass("bg-warning");
                $("#intellect").text(intellect+1);
                $("#coding").text(coding+1);
                $("#energy").text(energy-(60-endurance));
                    
                intellect = intellect + 1;
                coding = coding + 1;
                energy = energy-(60-endurance);

                setTimeout(() => { 
                    $("#study").removeClass("bg-warning");
                }, 800);
            }
        } else {
            $("#study").addClass("bg-danger");
            setTimeout(() => { 
                $("#study").removeClass("bg-danger");
            }, 800);
        }   
    }
    }); 
});