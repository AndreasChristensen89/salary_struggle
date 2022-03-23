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
        if (parseInt($(`#${skill}`).text()) >= randomNumber && level == 1) {
            success();
        } else {
            fail(skill);
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
        if (intellect+coding+charm >= randomNumber) {
            success();
        } else {
            fail("combine");
        } 
    }
    }); 
});

function success() {
    $("#level").text(level++);
    level++;

    $('.overview').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    $(".level-one").addClass("hide");
    $("#passed").removeClass("d-none");
    $('#bubble').css('opacity', '1');
    $('.action').off();

    setTimeout(() => {
        $('.overview').fadeToggle(100);
        $('#loading-overlay').fadeToggle(100);
    }, 2000);
}

function fail(skill) {
    $(`#agency_${skill}`).addClass("bg-danger");
    $("#energy").text("0");
    energy = 0;

    setTimeout(() => {
        $(`#agency_${skill}`).removeClass("bg-danger");
    }, 800);
}