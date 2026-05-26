from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect

from matching.models import CompatibilityScore
from profiles.models import Profile


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


@login_required
@subscription_required
def profile_view(request, profile_id):
    viewed_profile = get_object_or_404(Profile, id=profile_id)

    if viewed_profile.user == request.user:
        return redirect('profile_detail')
    
    if viewed_profile.profile_visibility == 'HI':
        return redirect('matching:matches')
    
    user_profile = request.user.profile
    score  = CompatibilityScore.objects.filter(
        Q(from_profile=user_profile, to_profile=viewed_profile) |
        Q(from_profile=viewed_profile, to_profile=user_profile)
    ).first()

    return render(request, 'matching/profile_view.html',{
        'viewed_profile': viewed_profile,
        'score': score,
    })