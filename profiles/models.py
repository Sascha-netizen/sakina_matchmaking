from datetime import date
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


def validate_age(value):
    today = date.today()
    age = today.year - value.year - (
        (today.month, today.day) < (value.month, value.day)
    )
    if age < 18:
        raise ValidationError("Users must be at least 18 years old.")


class Profile(models.Model):

    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

    class Sect(models.TextChoices):
        SUNNI = 'SU', 'Sunni'
        SHIA = 'SH', 'Shia'
        OTHER = 'OT', 'Other'
        PREFER_NOT = 'PN', 'Prefer not to say'

    class MaritalStatus(models.TextChoices):
        SINGLE = 'SI', 'Single'
        DIVORCED = 'DI', 'Divorced'
        WIDOWED = 'WI', 'Widowed'

    class Religiosity(models.IntegerChoices):
        CULTURAL = 1, 'Cultural'
        PRACTICING_SOME = 2, 'Practicing sometimes'
        PRACTICING = 3, 'Practicing'
        DEVOUT = 4, 'Devout'
        SCHOLAR = 5, 'Scholar'

    class Education(models.TextChoices):
        SECONDARY = 'SE', 'Secondary'
        VOCATIONAL_OR_TRADE = 'VT', 'Vocational Training or Learned a Trade'
        HIGH_SCHOOL_DIPLOMA = 'HD', 'High-School Diploma'
        BACHELOR = 'BA', 'Bachelors'
        MASTER = 'MA', 'Masters'
        DOCTORATE = 'PHD', 'Doctorate'
        OTHER = 'OT', 'Other'

    class Visibility(models.TextChoices):
        PUBLIC = 'PU', 'Public'
        SUBSCRIBERS = 'SB', 'Subscribers only'
        HIDDEN = 'HI', 'Hidden'

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    date_of_birth = models.DateField(
        validators=[validate_age]
    )
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        db_index=True
    )
    ethnicity = models.CharField(max_length=100)
    country = models.CharField(
        max_length=100,
        db_index=True
    )
    city = models.CharField(
        max_length=100,
        db_index=True
    )
    sect = models.CharField(
        max_length=2,
        choices=Sect.choices,
        db_index=True
    )
    religiosity_level = models.IntegerField(
        choices=Religiosity.choices,
        db_index=True
    )
    marital_status = models.CharField(
        max_length=2,
        choices=MaritalStatus.choices,
        db_index=True
    )
    has_children = models.BooleanField(default=False)
    wants_children = models.BooleanField(default=True)
    education = models.CharField(
        max_length=3,
        choices=Education.choices
    )
    occupation = models.CharField(max_length=100)
    languages = models.CharField(max_length=150)
    bio = models.TextField(blank=True)
    photo = models.ImageField(
        upload_to='profile_photos/',
        blank=True,
        null=True
    )
    wali_preference = models.BooleanField(default=False)
    profile_visibility = models.CharField(
        max_length=2,
        choices=Visibility.choices,
        default=Visibility.PUBLIC,
        db_index=True
    )
    completed = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )

    def __str__(self):
        return f"{self.user.username}'s profile"