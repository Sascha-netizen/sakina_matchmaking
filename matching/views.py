from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone

from matching.models import CompatibilityScore, Message
from profiles.models import Profile
from matching.algorithm import calculate_compatibility


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
    score = CompatibilityScore.objects.filter(
        Q(from_profile=user_profile, to_profile=viewed_profile) |
        Q(from_profile=viewed_profile, to_profile=user_profile)
    ).first()

    return render(request, 'matching/profile_view.html', {
        'viewed_profile': viewed_profile,
        'score': score,
    })


@login_required
@subscription_required
def inbox(request):
    messages = Message.objects.filter(
        recipient=request.user
    ).select_related('sender').order_by('-sent_at')

    return render(request, 'matching/inbox.html', {
        'messages': messages,
    })


@login_required
@subscription_required
def conversation(request, user_id):
    other_user = get_object_or_404(
        Profile, id=user_id
    ).user

    messages = Message.objects.filter(
        Q(sender=request.user, recipient=other_user) |
        Q(sender=other_user, recipient=request.user)
    ).order_by('sent_at')

    # Mark unread messages as read
    messages.filter(
        recipient=request.user,
        read_at__isnull=True
    ).update(read_at=timezone.now())

    if request.method == 'POST':
        body = request.POST.get('body', '').strip()
        if body:
            Message.objects.create(
                sender=request.user,
                recipient=other_user,
                body=body
            )
        return redirect('matching:conversation', user_id=user_id)

    return render(request, 'matching/conversation.html', {
        'messages': messages,
        'other_user': other_user,
    })

@login_required
@subscription_required
def refresh_matches(request):
    profile = request.user.profile
    profiles = Profile.objects.filter(
        completed=True
    ).exclude(user=request.user)

    for other_profile in profiles:
        score = calculate_compatibility(profile, other_profile)
        if score is None:
            continue
        # Check both directions
        existing = CompatibilityScore.objects.filter(
            Q(from_profile=profile, to_profile=other_profile) |
            Q(from_profile=other_profile, to_profile=profile)
        ).first()

        if existing:
            existing.score = score
            existing.save()
        else:
            CompatibilityScore.objects.create(
                from_profile=profile,
                to_profile=other_profile,
                score=score
            )

    return redirect('matching:matches')