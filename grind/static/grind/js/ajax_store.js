// get the CSRF token
const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;
// remove the token from the DOM
document.querySelector('[name=csrfmiddlewaretoken]').remove();

var money = parseInt($("#money").text());

$(".item-buy").click(function() {
    let itemID = parseInt($(this).attr("value"));
    let permanent = $(this).attr("permanent");
    let price = parseInt($(this).attr("price"));

    $.ajax({
    type: "POST",
    url: `add-item/${itemID}/`,
    headers: {'X-CSRFToken': csrf},
    data: {
        'item_id': itemID,
    },
    success: function(){
        if (money >= price) {
            if (permanent == "True") {
                let curr_html = $(`#item${itemID}`).html();
                $(`#item${itemID}`).html(curr_html + " <strong>Purchased</strong>");
            } else {
                $(`#item${itemID}`).addClass("bg-success");
                setTimeout(() => {
                    $(`#item${itemID}`).removeClass("bg-success");
                }, 800);
            }
        } else {
            $(`#item${itemID}`).addClass("bg-danger");
            setTimeout(() => {
                $(`#item${itemID}`).removeClass("bg-danger");
            }, 800);
        }
        }
    }); 
});
