const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;

document.querySelector('[name=csrfmiddlewaretoken]').remove();

var charm = parseInt($("#charm").html());
var money = parseInt($("#money").html());
var energy = parseInt($("#energy").html());
var endurance = parseInt($("#endurance").html());

$("#drinkButton").click(function() {
    $.ajax({
        type: "POST",
        url: "/grind/ajax-drink/",
        headers: {'X-CSRFToken': csrf},
        data: {
            'updateCharm': 2
        },
        success: function(){
            $("#drinkButton").addClass("bg-success");
            $("#charm").html(charm+2);
            charm = charm+2;
            $("#money").html(money-1000);
            money = money-1000;
            $("#energy").html(energy-(40-endurance));
            energy = energy-(40-endurance);
        }
    });
});