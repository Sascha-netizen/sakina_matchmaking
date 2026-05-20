from django.contrib.auth.models import AbstractUser
from django.conf import settings
import stripe


class User(AbstractUser):

    def delete(self, *args, **kwargs):
        from subscriptions.models import Subscription
        stripe.api_key = settings.STRIPE_SECRET_KEY
        for subscription in self.subscriptions.filter(
            status=Subscription.Status.ACTIVE
        ):
            try:
                stripe.Subscription.cancel(
                    subscription.stripe_subscription_id
                )
            except stripe.error.StripeError:
                pass
        super().delete(*args, **kwargs)