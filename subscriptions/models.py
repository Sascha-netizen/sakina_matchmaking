from django.conf import settings
from django.db import models


class Subscription(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Active'
        CANCELLED = 'cancelled', 'Cancelled'
        EXPIRED = 'expired', 'Expired'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='subscriptions'
    )
    stripe_customer_id = models.CharField(
        max_length=255,
        blank=True
    )
    stripe_subscription_id = models.CharField(
        max_length=255,
        blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.CANCELLED,
        db_index=True
    )
    started_at = models.DateTimeField(
        null=True,
        blank=True
    )

    expires_at = models.DateTimeField(
        null=True,
        blank=True
    )
    cancelled_at = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['-started_at']

    @property
    def is_active(self):
        return self.status == self.Status.ACTIVE

    def __str__(self):
        return f"{self.user.email} - {self.status}"
