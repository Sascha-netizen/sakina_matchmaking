from matching.models import Message


def unread_message_count(request):
    """Return the number of unread messages for the current user."""
    if request.user.is_authenticated:
        count = Message.objects.filter(
            recipient=request.user,
            read_at__isnull=True
        ).count()
        return {'unread_message_count': count}
    return {'unread_message_count': 0}