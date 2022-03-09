/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {   // when the user clicks the submit button the default is prevented...
    ev.preventDefault();
    card.update({ 'disabled': true});   // ... disables card element..
    $('#submit-button').attr('disabled', true); // ... and submit button to prevent multiple submissions
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);  // an triggers loading overlay...

    // ... then we create four vars to capture the form data
    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
    };
    var url = '/premium/cache_checkout_data/'; // we can't put these in the payment intent here...

    // ... so instead we post it to the cache_checkout_data view...
    $.post(url, postData).done(function () {    // ... done method used to wait for a response that payment intent was updated...
        stripe.confirmCardPayment(clientSecret, {   // ... when we have 200 response then we call the confirmCardPayment()
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    email: $.trim(form.email.value),
                    }
                }
            },
        ).then(function(result) {
            if (result.error) { // if ther's an error...
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html); // ... then error displayed... 
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100); // ... overlay will be hidden...
                card.update({ 'disabled': false}); // ... card element re-enabled...  
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {   // will be triggered if we get a 400 response
        // just reload the page, the error will be in django messages
        location.reload();
    })
});