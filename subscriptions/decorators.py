from functools import wraps
from django.shortcuts import redirect
from .models import Subscription


def subscription_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account_login')
        has_active_sub = Subscription.objects.filter(
            user=request.user,
            status=Subscription.Status.ACTIVE
        ).exists()
        if not has_active_sub:
            return redirect('subscriptions:checkout')
        return view_func(request, *args, **kwargs)
    return wrapper
