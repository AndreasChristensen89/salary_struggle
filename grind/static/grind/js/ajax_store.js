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

            if (element == "energy" && energy > 180) {
                $("#game-message").text("That's enough energy for one day");
                $("#game-message-container").removeClass("d-none");

                setTimeout(() => { 
                    $("#game-message-container").addClass("d-none");
                }, 1500);
            } else {
                // the current stat level
                let curr_number = parseInt($(`#${element}`).text());
                $("#money").html(`<i class="fas fa-yen-sign ml-1"></i> ${money - price}`);
                money = money - price;
                // Adds stat to old stat
                if (element == "energy") {
                    $("#energy").html(`<i class="fas fa-bolt mx-1"></i> ${curr_number + increase}`);
                    energy += 20;
                } else {
                    $(`#${element}`).text(curr_number + increase);
                }

                // if item is permanent disable click and add "Owned"
                if (permanent == "True") {
                    let curr_html = $(`#item${itemID}`).html();
                    $(`#item${itemID}`).html(curr_html + " <strong>Owned</strong>");
                    $(`#item${itemID}`).off("click");

                    $('#itemPermanent').removeClass("hide");
                }
                let name = $(`#itemName${itemID}`).text();
                // capitalise first char in element
                element = element.charAt(0).toUpperCase() + element.slice(1);
                // add text to overlay
                $("#itemBought").text(`You bought the ${name}`);
                $("#itemEffect").text(`${element} + ${increase}`)

                // show overlay
                $('.overview').fadeToggle(100);
                $(".loading-overlay").fadeToggle(100);

                setTimeout(() => { 
                    $('.overview').fadeToggle(100);
                    $(".loading-overlay").fadeToggle(100);
                    if (permanent) {
                        $('#itemPermanent').addClass("hide");
                    }
                }, 2000);
            }
            
        } else {
            $("#game-message").html(`You need <i class="fas fa-yen-sign"></i>${price}`);
            $("#game-message-container").removeClass("d-none");

            setTimeout(() => { 
                $("#game-message-container").addClass("d-none");
            }, 1500);
        }
        }
    }); 
});
