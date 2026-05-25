import random
from datetime import date

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from faker import Faker

from profiles.models import Profile

fake = Faker()

User = get_user_model()

MALE_NAMES = [
    'Ahmed', 'Ali', 'Omar', 'Yusuf', 'Ibrahim', 'Khalid', 'Hassan',
    'Tariq', 'Bilal', 'Hamza', 'Samir', 'Idris', 'Kareem', 'Nabil',
    'Rashid', 'Zaid', 'Faris', 'Amir', 'Suleiman', 'Mustafa',
]

FEMALE_NAMES = [
    'Fatima', 'Aisha', 'Maryam', 'Zainab', 'Nour', 'Sara', 'Layla',
    'Hana', 'Yasmin', 'Amira', 'Salma', 'Dina', 'Rania', 'Lina',
    'Nadia', 'Samira', 'Hafsa', 'Khadija', 'Sumaya', 'Iman',
]

LAST_NAMES = [
    'Al-Amin', 'Hassan', 'Ibrahim', 'Malik', 'Osman', 'Rahman',
    'Saleh', 'Sharif', 'Sultan', 'Yilmaz', 'Demir', 'Celik',
    'Bouazza', 'Benali', 'Mansouri', 'Khalil', 'Nasser', 'Haddad',
    'Saeed', 'Karimi',
]

LOCATIONS = [
    ('Germany', 'Berlin'),
    ('Germany', 'Hamburg'),
    ('Germany', 'Munich'),
    ('Germany', 'Frankfurt'),
    ('United Kingdom', 'London'),
    ('United Kingdom', 'Birmingham'),
    ('United Kingdom', 'Manchester'),
    ('France', 'Paris'),
    ('France', 'Lyon'),
    ('Netherlands', 'Amsterdam'),
    ('Netherlands', 'Rotterdam'),
    ('Belgium', 'Brussels'),
    ('Austria', 'Vienna'),
    ('Sweden', 'Stockholm'),
    ('Denmark', 'Copenhagen'),
]

LANGUAGES = [
    'Arabic', 'English', 'German', 'French', 'Turkish',
    'Urdu', 'Dutch', 'Swedish', 'Persian',
]

ETHNICITIES = [
    'Arab', 'Turkish', 'South Asian', 'North African',
    'West African', 'Persian', 'Somali', 'Kurdish', 'Mixed',
]


def random_dob(min_age=22, max_age=45):
    today = date.today()
    start = date(today.year - max_age, 1, 1)
    end = date(today.year - min_age, 12, 31)
    return fake.date_between(start_date=start, end_date=end)


def random_languages():
    count = random.randint(1, 3)
    return ', '.join(random.sample(LANGUAGES, count))


class Command(BaseCommand):
    help = 'Seed the database with fake Muslim European profiles'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=50,
            help='Number of profiles to create (default: 50)',
        )

    def handle(self, *args, **options):
        count = options['count']
        created = 0

        for i in range(count):
            gender = random.choice(['M', 'F'])

            if gender == 'M':
                first_name = random.choice(MALE_NAMES)
            else:
                first_name = random.choice(FEMALE_NAMES)

            last_name = random.choice(LAST_NAMES)
            username = f"{first_name.lower()}{last_name.lower().replace('-', '')}{i}"
            email = f"{username}@example.com"

            if User.objects.filter(username=username).exists():
                continue

            user = User.objects.create_user(
                username=username,
                email=email,
                password='testpass123',
                first_name=first_name,
                last_name=last_name,
            )

            country, city = random.choice(LOCATIONS)

            marital_choices = ['SI', 'DI', 'WI']
            if gender == 'M':
                marital_choices.append('MR')

            Profile.objects.create(
                user=user,
                date_of_birth=random_dob(),
                gender=gender,
                ethnicity=random.choice(ETHNICITIES),
                country=country,
                city=city,
                sect=random.choice(['SU', 'SH', 'OT']),
                religiosity_level=random.randint(1, 5),
                marital_status=random.choice(marital_choices),
                has_children=random.choice([True, False]),
                wants_children=random.choice([True, False]),
                education=random.choice(['SE', 'VT', 'HD', 'BA', 'MA', 'PHD']),
                occupation=fake.job(),
                languages=random_languages(),
                bio=fake.text(max_nb_chars=200),
                wali_preference=random.choice([True, False]),
                profile_visibility=random.choice(['PU', 'SB']),
                completed=True,
            )

            created += 1

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created} profiles')
        )