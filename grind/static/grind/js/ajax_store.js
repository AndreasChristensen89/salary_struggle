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
            $("#money").html(`<i class="fas fa-yen-sign ml-1"></i> ${money + price}`);
            money = money - price;
            // Adds stat to old stat
            if (element == "energy") {
                $("#energy").html(`<i class="fas fa-bolt mx-1"></i> ${curr_number + increase}`);
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
            $("#itemBought").text(`You bought the ${name}`);
            $("#itemEffect").text(`Your ${element} went up with ${increase}`)
            $('.overview').fadeToggle(100);
            $(".loading-overlay").fadeToggle(100);

            setTimeout(() => { 
                $('.overview').fadeToggle(100);
                $(".loading-overlay").fadeToggle(100);
                if (permanent) {
                    $('#itemPermanent').addClass("hide");
                }
            }, 3000);

        } else {
            $(`#item${itemID}`).addClass("bg-danger");
            setTimeout(() => {
                $(`#item${itemID}`).removeClass("bg-danger");
            }, 800);
        }
        }
    }); 
});
