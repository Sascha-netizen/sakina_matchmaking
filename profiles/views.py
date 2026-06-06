from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
import stripe

from subscriptions.models import Subscription
from .forms import ProfileForm, ProfileEditForm
from .models import Profile
from subscriptions.decorators import subscription_required


@login_required
def create_profile(request):
    if hasattr(request.user, 'profile'):
        return redirect('profile_edit')
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.completed = True
            profile.save()
            return redirect('profile_detail')
    else:
        form = ProfileForm()
    return render(request, 'profiles/create_profile.html', {'form': form})


@login_required
@subscription_required
def profile_detail(request):
    if not hasattr(request.user, 'profile'):
        return redirect('profile_create')
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'profiles/profile_detail.html', {'profile': profile})


@login_required
@subscription_required
def profile_edit(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail')
    else:
        form = ProfileEditForm(instance=profile)
    return render(request, 'profiles/profile_edit.html', {'form': form})


@login_required
def delete_account(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        try:
            with transaction.atomic():
                if profile.photo:
                    profile.photo.delete(save=False)
                subscriptions = Subscription.objects.filter(
                    user=request.user,
                    status='active'
                )
                for subscription in subscriptions:
                    if subscription.stripe_subscription_id:
                        stripe.Subscription.cancel(
                            subscription.stripe_subscription_id
                        )
                    subscription.status = 'cancelled'
                    subscription.cancelled_at = timezone.now()
                    subscription.save()
                    send_mail(
                        subject='Your Sakina subscription has been cancelled',
                        message=(
                            'Assalamu Alaykum,\n\n'
                            'Your Sakina subscription has been cancelled. '
                            'You will not be charged again.\n\n'
                            'You can resubscribe at any time at '
                            'https://sakina-matchmaking-7bcbb6fbb05b.herokuapp.com\n\n'
                            'Barakallahu feekum,\n'
                            'The Sakina Team'
                        ),
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[request.user.email],
                        fail_silently=True,
                    )
                request.user.delete()
            messages.success(
                request,
                'Your account has been deleted successfully.'
            )
            return redirect('account_login')
        except Exception:
            messages.error(
                request,
                'Account deletion failed. Please try again.'
            )
            return redirect('profile_detail')
    return render(
        request,
        'profiles/delete_account.html',
        {'profile': profile}
    )