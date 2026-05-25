from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from matching.models import CompatibilityScore


def subscription_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account_login')
        if not request.user.subscriptions.filter(status='active').exists():
            return redirect('subscriptions:checkout')
        return view_func(request, *args, **kwargs)
    return wrapper


@login_required
@subscription_required
def matches(request):
    profile = request.user.profile

    scores = CompatibilityScore.objects.filter(
        Q(from_profile=profile) | Q(to_profile=profile)
    ).select_related(
        'from_profile__user', 'to_profile__user'
    ).order_by('-score')

    return render(request, 'matching/matches.html', {
        'scores': scores,
        'profile': profile,
    })