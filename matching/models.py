from django.db import models
from profiles.models import Profile


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
