import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from profiles.models import Profile


class Command(BaseCommand):
    help = 'Add randomuser.me photos to existing profiles without photos'

    def handle(self, *args, **options):
        profiles = Profile.objects.filter(photo='')
        total = profiles.count()
        updated = 0

        self.stdout.write(f'Found {total} profiles without photos')

        for profile in profiles:
            gender = 'male' if profile.gender == 'M' else 'female'
            username = profile.user.username

            try:
                r = requests.get(
                    f'https://randomuser.me/api/?gender={gender}&nat=gb,de,fr,tr',
                    timeout=5
                )
                if r.status_code == 200:
                    photo_url = r.json()['results'][0]['picture']['large']
                    photo_response = requests.get(photo_url, timeout=5)
                    if photo_response.status_code == 200:
                        profile.photo.save(
                            f'{username}.jpg',
                            ContentFile(photo_response.content),
                            save=True
                        )
                        updated += 1
                        self.stdout.write(f'  {updated}/{total}: {username}')
            except Exception as e:
                self.stdout.write(f'  Skipped {username}: {e}')

        self.stdout.write(
            self.style.SUCCESS(f'Done. {updated} photos added.')
        )