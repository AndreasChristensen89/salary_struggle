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

$("#agencyIntellect").click(function() {
    let randomIntellect = Math.floor(Math.random() * 20) + 1;
    let skill = $(this).attr("value");
    
    $.ajax({
    type: "POST",
    url: "/grind/agency-intellect/",
    headers: {'X-CSRFToken': csrf},
    data: {
        'random_number': randomIntellect,
        'skill': skill
    },
    success: function(){
        if (intellect >= randomIntellect) {
            $("#level").text(level++);
            level++;

            $('.overview').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);

            setTimeout(() => { 
                $('.overview').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
            }, 30000);
        } else {
            $("#agencyIntellect").addClass("bg-danger");
            $("#energy").text("0");
            energy = 0;

            setTimeout(() => { 
                $("#agencyIntellect").removeClass("bg-danger");
            }, 800);
        } 
    }
    }); 
});