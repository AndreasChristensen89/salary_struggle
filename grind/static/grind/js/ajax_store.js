// get the CSRF token
const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;
// remove the token from the DOM
document.querySelector('[name=csrfmiddlewaretoken]').remove();

var money = parseInt($("#money").text());
var charm = parseInt($("#charm").text());
var energy = parseInt($("#energy").text());
var endurance = parseInt($("#endurance").text());
var intellect = parseInt($("#intellect").text());
var coding = parseInt($("#coding").text());

$(".item-buy").click(function() {
    let itemID = parseInt($(this).attr("value"));
    let permanent = $(this).attr("permanent");
    let price = parseInt($(this).attr("price"));

    $.ajax({
    type: "POST",
    url: "/grind/add-item/",
    headers: {'X-CSRFToken': csrf},
    data: {
        'item_id': itemID,
    },
    success: function(){
        if (money >= price) {
            // how much the stat increases
            let increase = parseInt($(`#item${itemID}stat`).text());
            // name of the stat
            let element = $(`#item${itemID}stat`).attr("value");
            // the current stat level
            let curr_number = parseInt($(`#${element}`).text());
            // Adds stat to old stat
            $(`#${element}`).text(curr_number + increase);
            $(`#item${itemID}`).addClass("bg-success");

            // if item is permanent 
            if (permanent == "True") {
                let curr_html = $(`#item${itemID}`).html();
                $(`#item${itemID}`).html(curr_html + " <strong>Owned</strong>");
                $(`#item${itemID}`).off("click");
            }

            setTimeout(() => {
                $(`#item${itemID}`).removeClass("bg-success");
            }, 600);

            

        } else {
            $(`#item${itemID}`).addClass("bg-danger");
            setTimeout(() => {
                $(`#item${itemID}`).removeClass("bg-danger");
            }, 800);
        }
        }
    }); 
});
