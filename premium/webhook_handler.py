from django.http import HttpResponse


class StripeWHHandler:
    """Handle webhooks from Stripe"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handles webhook events
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
