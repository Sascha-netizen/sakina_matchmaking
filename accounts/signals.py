from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created and instance.email:
        send_mail(
            subject='Welcome to Sakina — سكينة',
            message=(
                'Assalamu Alaykum,\n\n'
                'Thank you for registering with Sakina — a dignified '
                'matchmaking platform for practising Muslims in Europe.\n\n'
                'To get started, complete your profile and subscribe to '
                'access your compatibility matches.\n\n'
                'Visit Sakina: '
                'https://sakina-matchmaking-7bcbb6fbb05b.herokuapp.com\n\n'
                'Barakallahu feekum,\n'
                'The Sakina Team'
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email],
            fail_silently=True,
        )