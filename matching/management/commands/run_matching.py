from itertools import combinations

from django.core.management.base import BaseCommand

from matching.algorithm import calculate_compatibility
from matching.models import CompatibilityScore
from profiles.models import Profile


class Command(BaseCommand):
    help = 'Run compatibility algorithm across all profile pairs'

    def handle(self, *args, **options):
        profiles = list(Profile.objects.filter(completed=True))
        total = 0
        skipped = 0

        for profile_a, profile_b in combinations(profiles, 2):
            score = calculate_compatibility(profile_a, profile_b)

            if score is None:
                skipped += 1
                continue

            CompatibilityScore.objects.update_or_create(
                from_profile=profile_a,
                to_profile=profile_b,
                defaults={'score': score},
            )

            total += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'Done. {total} scores saved, {skipped} pairs skipped.'
            )
        )