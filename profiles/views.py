from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

# TODO: import Subscription and stripe once subscriptions app is built
# from subscriptions.models import Subscription
# import stripe

from .forms import ProfileForm
from .models import Profile


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
def profile_detail(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'profiles/profile_detail.html', {'profile': profile})


@login_required
def profile_edit(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profiles/profile_edit.html', {'form': form})


@login_required
def delete_account(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        try:
            with transaction.atomic():
                if profile.photo:
                    profile.photo.delete(save=False)
                # TODO: uncomment once subscriptions app is built
                # subscriptions = Subscription.objects.filter(
                #     user=request.user,
                #     status='active'
                # )
                # for subscription in subscriptions:
                #     if subscription.stripe_subscription_id:
                #         stripe.Subscription.cancel(
                #             subscription.stripe_subscription_id
                #         )
                #     subscription.status = 'cancelled'
                #     subscription.cancelled_at = timezone.now()
                #     subscription.save()
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