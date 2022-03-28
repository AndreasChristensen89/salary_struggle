// get the CSRF token
const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;
// remove the token from the DOM
document.querySelector('[name=csrfmiddlewaretoken]').remove();

var intellect = parseInt($("#intellect").text());
var energy = parseInt($("#energy").text());
var coding = parseInt($("#coding").text());
var charm = parseInt($("#charm").text());
var endurance = parseInt($("#endurance").text());
var level = parseInt($("#level").text());

$(".ask-interview").click(function() {
    let randomNumber = Math.floor(Math.random() * 20) + 1;
    let skill = $(this).attr("value");
    
    $.ajax({
    type: "POST",
    url: "/grind/agency-skill/",
    headers: {'X-CSRFToken': csrf},
    data: {
        'random_number': randomNumber,
        'skill': skill
    },
    success: function(){
        if (energy >= 100) {
            if (parseInt($(`#${skill}`).text()) >= randomNumber && level == 1) {
                success();
            } else {
                fail(skill);
            } 
        } else {
            $("#game-message").text("You need 100 energy");
            $("#game-message-container").removeClass("d-none");

            setTimeout(() => { 
                $("#game-message-container").addClass("d-none");
            }, 1500);
        }     
    }
    }); 
});

$("#agency_combine").click(function() {
    let randomNumber = Math.floor(Math.random() * 60) + 1;
    
    $.ajax({
    type: "POST",
    url: "/grind/agency-combine/",
    headers: {'X-CSRFToken': csrf},
    data: {
        'random_number': randomNumber,
    },
    success: function(){
        if (energy >= 100) {
            if (intellect+coding+charm >= randomNumber && level == 1) {
                success();
            } else {
                fail();
            }
            
        } else {
            $("#game-message").text("You need 100 energy");
            $("#game-message-container").removeClass("d-none");

            setTimeout(() => { 
                $("#game-message-container").addClass("d-none");
            }, 1500);
        } 
    }
    }); 
});

function success() {
    $("#level").text(level++);
    level++;

    $('.overview').fadeToggle(100);
    $(".loading-overlay").eq(0).fadeToggle(100);

    setTimeout(() => { 
        $('.overview').fadeToggle(100);
        $(".loading-overlay").eq(0).fadeToggle(100);
    }, 2500);

    $(".level-one").addClass("hide");
    $("#passed").removeClass("d-none");
    $('#bubble-agency').css('opacity', '1');
    $('.agency-action-row').addClass('d-none');
    $('.action').off();

}

function fail() {
    $("#energy").html(`<i class="fas fa-bolt mx-1"></i> 0`);
    energy = 0;

    $('.overview').fadeToggle(100);
    $(".loading-overlay").eq(1).fadeToggle(100);

    setTimeout(() => { 
        $('.overview').fadeToggle(100);
        $(".loading-overlay").eq(1).fadeToggle(100);
    }, 2500);

}