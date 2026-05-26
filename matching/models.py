from django.db import models
from profiles.models import Profile
from django.conf import settings


class CompatibilityScore(models.Model):
    from_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='scores_given'
    )
    to_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='scores_received'
    )
    score = models.IntegerField()
    calculated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [('from_profile', 'to_profile')]
        ordering = ['-score']

    def __str__(self):
        return (
            f"{self.from_profile} → {self.to_profile}: {self.score}"
        )


class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='messages_sent'
    )
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='messages_received'
    )
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['sent_at']
    
    def __str__(self):
        return f"{self.sender} → {self.recipient}: {self.sent_at:%Y-%m-%d %H:%M}"
