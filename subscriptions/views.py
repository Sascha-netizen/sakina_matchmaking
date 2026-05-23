import stripe
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Subscription

stripe.api_key = settings.STRIPE_SECRET_KEY
User = get_user_model()


@login_required
def create_checkout_session(request):
    already_subscribed = Subscription.objects.filter(
        user=request.user,
        status=Subscription.Status.ACTIVE,
    ).exists()
    if already_subscribed:
        return redirect('subscriptions:success')
    
    checkout_session = stripe.checkout.Session.create(
        customer_email=request.user.email,
        payment_method_types=['card'],
        line_items=[{
            'price': settings.STRIPE_PRICE_ID,
            'quantity': 1,
        }],
        mode='subscription',
        success_url=request.build_absolute_uri('/profile/create/'),
        cancel_url=request.build_absolute_uri('/subscriptions/cancel/'),
    )
    return redirect(checkout_session.url)


@login_required
def subscription_success(request):
    return render(request, 'subscriptions/success.html')


@login_required
def subscription_cancel(request):
    return render(request, 'subscriptions/cancel.html')


@csrf_exempt
@require_POST
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WH_SECRET
        )
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        handle_checkout_completed(session)

    elif event['type'] == 'customer.subscription.deleted':
        subscription = event['data']['object']
        handle_subscription_deleted(subscription)

    elif event['type'] == 'invoice.payment_failed':
        invoice = event['data']['object']
        handle_payment_failed(invoice)

    return HttpResponse(status=200)


def handle_checkout_completed(session):
    customer_id = session.customer
    subscription_id = session.subscription
    customer_email = session.customer_email

    try:
        user = User.objects.get(email=customer_email)
    except User.DoesNotExist:
        return

    stripe_sub = stripe.Subscription.retrieve(subscription_id)
    expires_at = timezone.datetime.fromtimestamp(
        stripe_sub['items']['data'][0]['current_period_end'],
        tz=timezone.utc
    )

    Subscription.objects.get_or_create(
        stripe_subscription_id=subscription_id,
        defaults={
            'user': user,
            'stripe_customer_id': customer_id,
            'status': Subscription.Status.ACTIVE,
            'started_at': timezone.now(),
            'expires_at': expires_at,
        }
    )


def handle_subscription_deleted(stripe_sub):
    try:
        sub = Subscription.objects.get(
            stripe_subscription_id=stripe_sub.id
        )
        sub.status = Subscription.Status.CANCELLED
        sub.cancelled_at = timezone.now()
        sub.save()
    except Subscription.DoesNotExist:
        pass


def handle_payment_failed(invoice):
    subscription_id = invoice.subscription
    try:
        sub = Subscription.objects.get(
            stripe_subscription_id=subscription_id
        )
        sub.status = Subscription.Status.EXPIRED
        sub.save()
    except Subscription.DoesNotExist:
        pass