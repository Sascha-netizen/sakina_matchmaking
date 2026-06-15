# Sakina — سكينة

**Find Your Tranquility**

Sakina is a dignified matchmaking platform for practising Muslims in Europe. The name comes from the Arabic word سَكِينَة — the tranquility that settles in the heart when something feels right. It appears in the Quran in the context of peace bestowed by God, and in the hadith literature in the context of the peace found in a righteous spouse.

Most Muslim matrimonial platforms feel like CV exchanges. Sakina is built on a different premise: that compatibility in Islamic marriage is primarily theological and values-based, not demographic. The platform's compatibility algorithm reflects this — weighting sect and religiosity at 45% of the total score, with practical factors making up the remainder.

Sakina is built for practising Muslims living in Europe who are serious about marriage and want a platform that takes that seriousness for granted.

**Live site:** [sakina-matchmaking-7bcbb6fbb05b.herokuapp.com](https://sakina-matchmaking-7bcbb6fbb05b.herokuapp.com/)

**Repository:** [github.com/Sascha-netizen/sakina_matchmaking](https://github.com/Sascha-netizen/sakina_matchmaking)

---

## E-Commerce Business Model

Sakina operates as a **B2C (Business to Consumer)** subscription platform.

### Business Type
Direct-to-consumer. Sakina connects individual Muslim users seeking marriage partners. There is no intermediary — the platform is the service.

### Revenue Model
Users pay a monthly subscription fee of €9.99 to access the platform's core features: compatibility matches, profile browsing, and direct messaging. Registration and profile creation are free, ensuring users can evaluate the platform before committing.

### Core Business Intents
- Provide a faith-aligned, dignified alternative to generic dating platforms for Muslims in Europe
- Generate recurring revenue through Stripe-managed monthly subscriptions
- Build trust through privacy-first design and theologically informed matching

### Target Audience
Practising Muslims living in Europe — primarily in Germany, Austria, the UK, France, the Netherlands, and Spain — who are serious about finding a spouse through a halal, dignified process.

### Value Proposition
Unlike generic matrimonial sites, Sakina's algorithm prioritises theological compatibility. Unlike mainstream dating apps, Sakina is built with the seriousness that Islamic marriage deserves — no swiping, no casual browsing, no ambiguity about intent.

### Marketing Strategy
- **SEO**: Targeting keywords such as "Muslim matchmaking Europe", "halal matrimonial", "Islamic marriage platform", and "practising Muslims" in meta tags and page content
- **Social media**: Facebook Business Page targeting Muslim communities in Europe
- **Email marketing**: Newsletter via EmailOctopus to build an audience before and after launch
- **Word of mouth**: The platform's niche focus and dignified design are intended to generate organic referrals within Muslim communities

## Facebook Business Page

A Facebook Business Page was created for Sakina to support social media marketing efforts and reach Muslim communities across Europe.

![Sakina Facebook Page](docs/marketing/fb-live-cover-page.PNG)

![Sakina Facebook About](docs/marketing/fb-live-about-page.PNG)

---

## Agile Development

This project was managed using GitHub Projects with a Kanban board tracking all user stories from backlog to completion.

**Kanban board:** [Sakina Development](https://github.com/users/Sascha-netizen/projects/13)

## Architecture

### Colour Palette

[View on Coolors](https://coolors.co/f9f6f0-085041-1d9e75-e1f5ee-2c2c2a)

| Name | Hex | Use |
|------|-----|-----|
| Parchment | `#F9F6F0` | Background |
| Pine Teal | `#085041` | Primary |
| Seaweed | `#1D9E75` | Accent / CTA |
| Honeydew | `#E1F5EE` | Cards / panels |
| Graphite | `#2C2C2A` | Body text |

### Typography

| Role | Font | Weight |
|------|------|--------|
| Wordmark / UI | [Lato](https://fonts.google.com/specimen/Lato) | 300, 400, 700 |
| Arabic accent | [Amiri](https://fonts.google.com/specimen/Amiri) | 400, 700 |

Lato is used throughout the interface for its warmth and readability. Amiri is used sparingly — the Arabic wordmark سكينة — as a quiet cultural gesture, consistent with the platform's identity.


## User Stories

### US01 - User Registration
**MoSCoW: Must Have**

#### User Story
As a user, I can register an account, so that I can create a profile on Sakina.

#### Acceptance Criteria
* Given a user is on the registration page: when they submit valid details, then an account is created and they are redirected to complete their profile.
* Given a user submits invalid details: when the form is submitted, then appropriate error messages are displayed.

#### Tasks
- [x] Create registration view
- [x] Create registration template
- [x] Add URL pattern

---

### US02 - User Login
**MoSCoW: Must Have**

#### User Story
As a user, I can log in to my account, so that I can access my profile and matches.

#### Acceptance Criteria
* Given a registered user is on the login page: when they submit valid credentials, then they are logged in and redirected to their profile.
* Given a user submits invalid credentials: when the form is submitted, then an error message is displayed and access is denied.

#### Tasks
- [x] Create login view
- [x] Create logout view
- [x] Create login template
- [x] Add URL patterns

---

### US03 - User Logout
**MoSCoW: Must Have**

#### User Story
As a logged in user, I can log out of my account, so that my account is secure.

#### Acceptance Criteria
* Given a logged in user clicks logout: when the action is confirmed, then the session is ended and they are redirected to the homepage.

#### Tasks
- [x] Add logout URL pattern
- [x] Add logout link to navbar

---

### US04 - Create Profile
**MoSCoW: Must Have**

#### User Story
As a registered user, I can complete my profile with personal, faith and lifestyle details, so that I can be matched accurately.

#### Acceptance Criteria
* Given a logged in user is on the profile page: when they submit valid profile details, then the profile is saved and displayed correctly.
* Given a user submits incomplete required fields: when the form is submitted, then appropriate error messages are displayed.

#### Tasks
- [x] Create profile model
- [x] Create profile form
- [x] Create profile view
- [x] Create profile template

---

### US05 - Edit Profile
**MoSCoW: Must Have**

#### User Story
As a registered user, I can edit my profile, so that my information stays current.

#### Acceptance Criteria
* Given a logged in user is on the edit profile page: when they submit updated details, then the changes are saved and reflected immediately.
* Given a user attempts to edit another user's profile: when they access the URL directly, then access is denied.

#### Tasks
- [x] Create edit profile view
- [x] Create edit profile template
- [x] Add URL pattern

---

### US06 - Upload Profile Photo
**MoSCoW: Should Have**

#### User Story
As a registered user, I can upload a profile photo, so that my profile is complete and recognisable.

#### Acceptance Criteria
* Given a logged in user is on the profile page: when they upload a valid image, then the photo is saved and displayed on their profile.
* Given a user uploads an invalid file type: when the form is submitted, then an error message is displayed.

#### Tasks
- [x] Add image field to profile model
- [x] Configure AWS S3 for image hosting
- [x] Update profile form and template

---

### US07 - Subscribe
**MoSCoW: Must Have**

#### User Story
As a registered user, I can subscribe via a secure payment, so that I can access matches and messaging.

#### Acceptance Criteria
* Given a logged in user is on the subscription page: when they complete a valid payment, then their account is upgraded to subscriber status.
* Given a payment fails: when the transaction is declined, then an error message is displayed and access is not granted.

#### Tasks
- [x] Integrate Stripe
- [x] Create subscription view
- [x] Create subscription template
- [x] Handle Stripe webhooks

---

### US08 - View Subscription Status
**MoSCoW: Should Have**

#### User Story
As a subscriber, I can view my subscription status, so that I know when it expires.

#### Acceptance Criteria
* Given a logged in subscriber is on their profile page: when they view their account details, then their subscription status and expiry date are clearly displayed.

#### Tasks
- [x] Add subscription status to profile view
- [x] Display status in profile template

---

### US09 - Cancel Subscription
**MoSCoW: Should Have**

#### User Story
As a subscriber, I can cancel my subscription, so that I am in control of my payments.

#### Acceptance Criteria
* Given a subscriber is on their account page: when they cancel their subscription, then it is cancelled in Stripe and their subscriber status is updated accordingly.

#### Tasks
- [x] Create cancellation view
- [x] Handle cancellation webhook from Stripe
- [x] Update subscription status on cancellation

> Note: Subscription cancellation is also handled automatically on account deletion, which cancels the active Stripe subscription before removing the user.

---

### US10 - View Matches
**MoSCoW: Must Have**

#### User Story
As a subscriber, I can view my compatibility matches, so that I can find a suitable spouse.

#### Acceptance Criteria
* Given a logged in subscriber is on the matches page: when the page loads, then a list of compatible profiles is displayed ranked by compatibility score.
* Given a non-subscriber attempts to access the matches page: when they access the URL directly, then they are redirected to the subscription page.

#### Tasks
- [x] Create matching algorithm
- [x] Create matches view
- [x] Create matches template
- [x] Add URL pattern

---

### US11 - View Compatibility Score
**MoSCoW: Should Have**

#### User Story
As a subscriber, I can see a compatibility score with each match, so that I understand why they were suggested.

#### Acceptance Criteria
* Given a subscriber is viewing their matches: when each profile is displayed, then a compatibility score is shown alongside it.

#### Tasks
- [x] Calculate and store compatibility score
- [x] Display score in matches template

---

### US12 - Filter Matches
**MoSCoW: Should Have**

#### User Story
As a subscriber, I can filter my matches by location, age and sect, so that I can narrow my options.

#### Acceptance Criteria
* Given a subscriber is on the matches page: when they apply filters, then only profiles matching the selected criteria are displayed.

#### Tasks
- [x] Add filter form to matches view
- [x] Update matches queryset based on filters
- [x] Update matches template

---

### US13 - Express Interest
**MoSCoW: Should Have**

#### User Story
As a subscriber, I can express interest in a profile, so that the other member is notified.

#### Acceptance Criteria
* Given a subscriber is viewing a profile: when they click express interest, then the other member receives a notification.
* Given a subscriber has already expressed interest: when they view the same profile, then the button reflects this.

#### Tasks
- [ ] Create interest model
- [ ] Create interest view
- [ ] Add notification to recipient profile

> Note: On Sakina, interest is expressed through direct messaging rather than a separate like or interest button. This reflects the platform's dignified approach to matrimonial communication — a message requires intentionality and seriousness, which is more appropriate for the platform's audience and ethos.

---

### US14 - Send Message
**MoSCoW: Must Have**

#### User Story
As a subscriber, I can send a message to a match, so that we can begin communication.

#### Acceptance Criteria
* Given a subscriber is viewing a match's profile: when they send a message, then it appears in both users' inboxes.
* Given a non-subscriber attempts to send a message: when they access the URL directly, then access is denied.

#### Tasks
- [x] Create message model
- [x] Create message view
- [x] Create inbox template
- [x] Add URL pattern

---

### US15 - View Inbox
**MoSCoW: Must Have**

#### User Story
As a subscriber, I can view my inbox, so that I can read messages from my matches.

#### Acceptance Criteria
* Given a logged in subscriber is on the inbox page: when the page loads, then all received messages are displayed in chronological order.

#### Tasks
- [x] Create inbox view
- [x] Create inbox template
- [x] Add URL pattern

---

### US16 - Admin Profile Moderation
**MoSCoW: Must Have**

#### User Story
As an admin, I can manage and moderate user profiles, so that the platform remains safe and trustworthy.

#### Acceptance Criteria
* Given an admin is logged into the Django admin panel: when they access the profiles section, then they can view, edit and delete any profile.
* Given a non-admin attempts to access the admin panel: when they access the URL directly, then access is denied.

#### Tasks
- [x] Register profile model in admin
- [x] Configure admin display and filters


## Wireframes

Low-fidelity wireframes were produced prior to development to plan the core page layouts.

### Landing Page

![Landing page wireframe](docs/wireframes/sakina_landing_wireframe.png)

### Profile Page

![Profile page wireframe](docs/wireframes/sakina_profile_wireframe.png)

### Matches Page

![Matches page wireframe](docs/wireframes/sakina_profile_wireframe.png)


## Entity-Relationship Diagram (ERD)

### Accounts — Custom User

| Key | Field | Type |
|-----|-------|------|
| PK | id | int |
| | username | varchar |
| | email | varchar |
| | password | varchar |
| | date_joined | datetime |

> Extended from Django's `AbstractUser`:
> ```python
> class User(AbstractUser):
>     pass
> ```

---

### Profiles

| Key | Field | Type | Notes |
|-----|-------|------|-------|
| PK | id | int | |
| FK | user_id → User | OneToOne | CASCADE on delete |
| | date_of_birth | date | Validated: must be 18+ |
| | gender | TextChoices | Indexed |
| | ethnicity | varchar | Free text |
| | country | varchar | Indexed |
| | city | varchar | Indexed |
| | sect | TextChoices | Indexed |
| | religiosity_level | int (1–5) | IntegerChoices, indexed |
| | marital_status | TextChoices | Indexed |
| | has_children | boolean | Default: False |
| | wants_children | boolean | Default: True |
| | education | TextChoices | |
| | occupation | varchar | |
| | languages | varchar | |
| | bio | text | Optional |
| | photo | image | Optional, hosted on AWS S3 |
| | wali_preference | boolean | Default: False |
| | profile_visibility | TextChoices (public / subscribers / hidden) | Indexed, default: public |
| | completed | boolean | Default: False, indexed |
| | created_at | datetime | Auto, ordered desc |

> `age` is a computed property derived from `date_of_birth`, not a stored field.
---

### Subscriptions

| Key | Field | Type |
|-----|-------|------|
| PK | id | int |
| FK | user_id → User | ForeignKey |
| | stripe_customer_id | varchar |
| | stripe_subscription_id | varchar |
| | status | TextChoices (active / cancelled / expired) |
| | started_at | datetime |
| | expires_at | datetime |
| | cancelled_at | datetime (nullable) |

---

### Matching

#### CompatibilityScore

| Key | Field | Type |
|-----|-------|------|
| PK | id | int |
| FK | from_profile_id → Profile | ForeignKey |
| FK | to_profile_id → Profile | ForeignKey |
| | score | int (0–100) |
| | calculated_at | datetime |

#### Interest

| Key | Field | Type |
|-----|-------|------|
| PK | id | int |
| FK | from_profile_id → Profile | ForeignKey |
| FK | to_profile_id → Profile | ForeignKey |
| | status | TextChoices (pending / matched / rejected) |
| | created_at | datetime |

#### Message

| Key | Field | Type |
|-----|-------|------|
| PK | id | int |
| FK | sender_id → User | ForeignKey |
| FK | recipient_id → User | ForeignKey |
| | body | text |
| | sent_at | datetime |
| | read_at | datetime (nullable) |

---

### Home

No models — static views only.

---

### Relationships

| From | Cardinality | To |
|------|-------------|-----|
| User | 1 → 1 | Profile |
| User | 1 → many | Subscription |
| Profile | 1 → many | CompatibilityScore (as sender) |
| Profile | 1 → many | CompatibilityScore (as receiver) |
| Profile | 1 → many | Interest (as sender) |
| Profile | 1 → many | Interest (as receiver) |
| User | 1 → many | Message (as sender) |
| User | 1 → many | Message (as recipient) |

---

### Unique Constraints

| Model | Constraint | Reason |
|-------|------------|--------|
| CompatibilityScore | (from_profile_id, to_profile_id) | No duplicate scores between the same two profiles |
| CompatibilityScore | from_profile_id != to_profile_id | No self-matching |
| Message | sender_id != recipient_id | A user cannot message themselves |
| Interest | from_profile_id != to_profile_id | A user cannot express interest in themselves |
| Interest | (from_profile_id, to_profile_id) | A user can only express interest once |



## Matching Algorithm

Sakina's compatibility algorithm compares two profiles across eight weighted dimensions and returns a score between 0 and 100. A higher score indicates greater compatibility. Scores are stored in the `CompatibilityScore` model and used to rank matches for subscribed users.

The weights reflect a considered hierarchy of what matters most in Muslim matrimonial contexts. Theological alignment — sect and religiosity — accounts for 45% of the total score, reflecting the centrality of shared faith practice in Islamic marriage. Practical compatibility — location, children, marital status, education, language, and age — accounts for the remaining 55%. The algorithm does not attempt to replicate human judgment, but to surface profiles worth considering.

### Scoring Breakdown

| Dimension | Max Points | Logic |
|-----------|------------|-------|
| Sect | 25 | Exact match only |
| Religiosity | 20 | Exact match: 20 points; one level apart: 15 points; two levels apart: 8 points; three or more: 0 points |
| Location | 15 | Same city and country: 15 points; same country only: 10 points |
| Children | 15 | Wants children alignment: 10 points; has children alignment: 5 points |
| Marital status | 10 | See polygamy note below |
| Education | 7 | Exact match: 7 points; one level apart: 4 points; two or more levels apart: 0 points |
| Languages | 5 | Any shared language: 5 points |
| Age | 3 | Up to 3 years apart: 3 points; 4–7 years: 2 points; 8–12 years: 1 point; over 12: 0 points |
| **Total** | **100** | |

### On Polygamy

Islamic jurisprudence permits a man to have up to four wives simultaneously, subject to conditions of fairness and equal treatment. A woman, by contrast, may have only one husband. Sakina's algorithm reflects this asymmetry deliberately, even though the developer does not personally endorse the practice. Polygamy represents a specifically neo-traditionalist position that has regained traction in recent years, partly in response to a sense within some Muslim communities that their values are misunderstood or dismissed by mainstream Western culture. The rediscovery of the practice is, perhaps counterintuitively, sometimes promoted by women within these communities themselves.

A married man may be matched with a single woman at a reduced marital status score of 5 points rather than 10. A married woman is never matched with anyone other than her existing husband — the platform does not surface such pairings. This is not a technical oversight but a theologically informed design decision, consistent with the orthodox Muslim audience Sakina is built for.



### Implementation

```python
from datetime import date


EDUCATION_RANKS = {
    'SE': 1,
    'VT': 2,
    'HD': 3,
    'BA': 4,
    'MA': 5,
    'PHD': 6,
}


def calculate_age(date_of_birth):
    today = date.today()

    return (
        today.year
        - date_of_birth.year
        - (
            (today.month, today.day)
            < (date_of_birth.month, date_of_birth.day)
        )
    )


def normalise_languages(value):
    return {
        lang.strip().lower()
        for lang in value.split(',')
        if lang.strip()
    }


def is_match_eligible(profile_a, profile_b):

    # No self matching
    if profile_a.user_id == profile_b.user_id:
        return False

    # Profiles must be completed
    if not profile_a.completed or not profile_b.completed:
        return False

    # Hidden profiles excluded
    if profile_a.profile_visibility == 'HI':
        return False

    if profile_b.profile_visibility == 'HI':
        return False

    # Opposite sex only
    if profile_a.gender == profile_b.gender:
        return False

    # Married women excluded from matchmaking
    if (
        profile_a.gender == 'F'
        and profile_a.marital_status == 'MR'
    ):
        return False

    if (
        profile_b.gender == 'F'
        and profile_b.marital_status == 'MR'
    ):
        return False

    return True


def calculate_compatibility(profile_a, profile_b):

    if not is_match_eligible(profile_a, profile_b):
        return None

    score = 0

    # -------------------------
    # Sect (25)
    # -------------------------

    if profile_a.sect == profile_b.sect:
        score += 25

    # -------------------------
    # Religiosity (20)
    # -------------------------

    religiosity_diff = abs(
        profile_a.religiosity_level
        - profile_b.religiosity_level
    )

    if religiosity_diff == 0:
        score += 20

    elif religiosity_diff == 1:
        score += 15

    elif religiosity_diff == 2:
        score += 8

    # -------------------------
    # Location (15)
    # -------------------------

    if (
        profile_a.city.strip().lower()
        == profile_b.city.strip().lower()
        and
        profile_a.country.strip().lower()
        == profile_b.country.strip().lower()
    ):
        score += 15

    elif (
        profile_a.country.strip().lower()
        == profile_b.country.strip().lower()
    ):
        score += 10

    # -------------------------
    # Children & family goals (15)
    # -------------------------

    # Wants children (10)

    if (
        profile_a.wants_children
        == profile_b.wants_children
    ):
        score += 10

    # Existing children (5)

    if (
        profile_a.has_children
        == profile_b.has_children
    ):
        score += 5

    # -------------------------
    # Marital status (10)
    # -------------------------

    if (
        profile_a.marital_status
        == profile_b.marital_status
    ):
        score += 10

    # Married man + single woman

    elif (
        (
            profile_a.gender == 'M'
            and profile_a.marital_status == 'MR'
            and profile_b.gender == 'F'
            and profile_b.marital_status == 'SI'
        )
        or
        (
            profile_b.gender == 'M'
            and profile_b.marital_status == 'MR'
            and profile_a.gender == 'F'
            and profile_a.marital_status == 'SI'
        )
    ):
        score += 5

    # -------------------------
    # Education (7)
    # -------------------------

    education_a = EDUCATION_RANKS.get(profile_a.education)
    education_b = EDUCATION_RANKS.get(profile_b.education)

    if (
        education_a is not None
        and education_b is not None
    ):

        education_diff = abs(
            education_a - education_b
        )

        if education_diff == 0:
            score += 7

        elif education_diff == 1:
            score += 4

    # -------------------------
    # Languages (5)
    # -------------------------

    langs_a = normalise_languages(
        profile_a.languages
    )

    langs_b = normalise_languages(
        profile_b.languages
    )

    if langs_a & langs_b:
        score += 5

    # -------------------------
    # Age compatibility (3)
    # -------------------------

    age_a = calculate_age(
        profile_a.date_of_birth
    )

    age_b = calculate_age(
        profile_b.date_of_birth
    )

    age_diff = abs(age_a - age_b)

    if age_diff <= 3:
        score += 3

    elif age_diff <= 7:
        score += 2

    elif age_diff <= 12:
        score += 1

    return min(score, 100)
```

## Features

### Landing Page

Sakina's homepage introduces the platform to anonymous visitors with a clear value proposition and calls to action.

![Landing page](docs/testing/features/landing-page.png)

### User Registration

New users can register with a username, email, and password.

![Sign up page](docs/testing/features/sign-up-page.png)

### Authentication

Users sign in securely. A flash message confirms successful login and the navbar updates to show authenticated links.

![Sign in success](docs/testing/features/feature-sign-in-success.png)

### Stripe Subscription

After registration, users are directed to a Stripe checkout page to subscribe for €9.99 per month before accessing any features.

![Stripe checkout](docs/testing/features/feature-stripe-checkout.png)

### Create Profile

Subscribed users complete a detailed profile covering faith, background, family goals, and personal information. Age validation ensures users are 18 or over.

![Create profile](docs/testing/features/feature-create-profile.png)

![Age validation](docs/testing/features/age-validation.png)

### Profile Detail

Users can view their own profile with all sections displayed clearly, and access edit, matches, and account deletion options.

![Profile detail](docs/testing/features/feature-profile-detail-1.png)

![Profile detail lower](docs/testing/features/feature-profile-detail-2.png)

### Compatibility Matches

The matching algorithm calculates compatibility scores against all other profiles. Before running, the matches page shows an empty state. After refreshing, ranked matches appear with photos, key details, and scores.

![Matches empty](docs/testing/features/feature-matches-empty.png)

![Matches](docs/testing/features/feature-matches.png)

### Profile View

Subscribers can view another user's full profile, including their compatibility score.

![Profile match view](docs/testing/features/feature-profile-match.png)

### Messaging

Users can send a message directly from a match's profile page.

![Send message](docs/testing/features/feature-send-message.png)

### Conversation

The conversation view shows the full message thread between two users.

![Conversation](docs/testing/features/feature-conversation-1.png)

![Conversation reply](docs/testing/features/feature-conversation-reply-youssef.png)

### Inbox

The inbox displays all received messages. An unread count appears in the navbar when new messages arrive.

![Inbox notification](docs/testing/features/feature-inbox-notification-youssef.png)

![Inbox](docs/testing/features/feature-inbox-youssef.png)


## Technologies Used

### Languages
- Python 3.12
- HTML5
- CSS3
- JavaScript (minimal — EmailOctopus newsletter widget)

### Frameworks and Libraries
- [Django 4.2](https://www.djangoproject.com/) — main web framework
- [django-allauth 65.16.1](https://django-allauth.readthedocs.io/) — authentication, registration, and password reset
- [django-storages 1.14.6](https://django-storages.readthedocs.io/) — AWS S3 file storage
- [Stripe 15.1.0](https://stripe.com/docs/api) — payment processing and subscription management
- [python-dateutil 2.9.0](https://dateutil.readthedocs.io/) — age validation
- [Pillow 12.2.0](https://pillow.readthedocs.io/) — image handling
- [Faker 40.19.1](https://faker.readthedocs.io/) — seeding test profiles
- [Gunicorn 26.0.0](https://gunicorn.org/) — WSGI server for Heroku deployment
- [Whitenoise 6.12.0](https://whitenoise.readthedocs.io/) — static file serving
- [psycopg2 2.9.12](https://www.psycopg.org/) — PostgreSQL database adapter
- [dj-database-url 0.5.0](https://pypi.org/project/dj-database-url/) — database URL configuration for Heroku

### Database
- [PostgreSQL](https://www.postgresql.org/) — relational database
- [Neon](https://neon.tech/) — serverless PostgreSQL hosting

### Cloud Services
- [AWS S3](https://aws.amazon.com/s3/) — profile photo storage
- [Heroku](https://www.heroku.com/) — application deployment and hosting

### Email and Marketing
- [Gmail SMTP](https://support.google.com/mail/answer/7126229) — transactional emails (registration, subscription, cancellation)
- [EmailOctopus](https://emailoctopus.com/) — newsletter mailing list

### Frontend
- [Google Fonts — Lato](https://fonts.google.com/specimen/Lato) — primary UI font
- [Google Fonts — Amiri](https://fonts.google.com/specimen/Amiri) — Arabic wordmark

### Development Tools
- [Visual Studio Code](https://code.visualstudio.com/) — IDE
- [Git](https://git-scm.com/) — version control
- [GitHub](https://github.com/) — repository hosting
- [Coolors](https://coolors.co/) — colour palette generation
- [Claude](https://claude.ai/) — debugging assistance

## Testing

### Automated Testing

Automated tests are written using Django's built-in `TestCase` framework and are located in `matching/tests.py`. The test database is created and destroyed automatically each time the tests are run.

#### Running the Tests

From the project root, with your virtual environment activated:

```bash
python manage.py test
```

A successful run looks like this:
```
Found 11 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...........
----------------------------------------------------------------------
Ran 11 tests in 1.204s
OK
Destroying test database for alias 'default'...
```

Each dot represents a passing test.

#### What is Tested

##### Eligibility Rules (`IsMatchEligibleTests`)

Covers the conditions under which two profiles are excluded from matching entirely.

- A user is never matched with themselves
- Two profiles of the same gender are not matched
- An incomplete profile is excluded from matching
- A hidden profile is excluded from matching
- A married woman is never surfaced as a match

##### Compatibility Scoring (`CompatibilityScoreTests`)

Covers the scoring logic of the compatibility algorithm.

- Two highly compatible profiles score 80 or above
- Profiles from different sects score 75 or below
- Matching sect adds exactly 25 points to the score
- A married man matched with a single woman receives a reduced score
- No score exceeds 100
- Profiles sharing at least one language receive language points

### Manual Testing

#### Authentication

| Test | Action | Expected Result | Pass/Fail |
|------|--------|-----------------|-----------|
| Register | Submit valid details on Sign Up page | Account created, redirected to homepage | Pass |
| Register (invalid) | Submit mismatched passwords | Error message displayed | Pass |
| Login | Submit valid credentials | Signed in, redirected to homepage | Pass |
| Login (invalid) | Submit wrong password | Error message displayed | Pass |
| Logout | Click Sign Out | Session ended, redirected to homepage | Pass |
| Access signup when logged in | Navigate to `/accounts/signup/` while logged in | Redirected to homepage | Pass |
| Access protected page when logged out | Navigate to `/matching/matches/` while logged out | Redirected to Sign In page | Pass |
| Password reset request | Click "Reset it here" on Sign In page, enter email | Password reset email received | Pass |
| Password reset — set new password | Click link in reset email, enter new password | Password reset complete page displayed | Pass |

---

#### Payments

| Test | Action | Expected Result | Pass/Fail |
|------|--------|-----------------|-----------|
| Successful payment | Enter Stripe test card `4242 4242 4242 4242` | Subscription created, redirected to Create Profile | Pass |
| Failed payment | Enter Stripe test card `4000 0000 0000 0002` | Stripe displays "Your credit card was declined" | Pass |
| Payment cancelled | Click back arrow on Stripe checkout | Redirected to Payment Unsuccessful page with message "You have not been charged" | Pass |

---

#### Navigation

| Test | Action | Expected Result | Pass/Fail |
|------|--------|-----------------|-----------|
| Anonymous navigation | Visit homepage without logging in | Sign In and Sign Up links visible | Pass |
| Authenticated navigation | Log in | My Profile, Matches, Inbox, Sign Out links visible | Pass |
| 404 page | Navigate to non-existent URL | Custom 404 page displayed with Return Home button | Pass |
| All pages reachable | Navigate via links only | Every public page reachable from homepage | Pass |

---

### Payment Testing Screenshots

**Failed payment — Stripe decline message:**

![Stripe decline](docs/testing/payments/failed-payment-checkout-page.png)

**Failed payment — site response:**

![Payment unsuccessful](docs/testing/payments/failed-payment-redirect.png)

**Successful payment — redirect to Create Profile:**

![Successful payment](docs/testing/payments/payment-successful-profile-redirection.png)

#### Email Notifications

| Test | Action | Expected Result | Pass/Fail |
|------|--------|-----------------|-----------|
| Registration welcome email | Register a new account | Welcome email received | Pass |
| Subscription confirmation email | Complete Stripe payment | Subscription confirmation email received | Pass |
| Cancellation email | Delete account with active subscription | Cancellation email received | Pass |
| Newsletter welcome email | Sign up via footer newsletter form | Newsletter welcome email received | Pass |

**Registration welcome email:**

![Registration email](docs/testing/emails/email-registration.png)

**Subscription confirmation email:**

![Subscription confirmation email](docs/testing/emails/email-subscription.png)

**Cancellation email:**

![Cancellation email](docs/testing/emails/email-cancellation.png)

**Newsletter welcome email:**

![Newsletter welcome email](docs/testing/emails/email-newsletter.png)

#### Password Reset Screenshots

**Password reset form:**

![Password reset form](docs/testing/passwords/password-reset-form.PNG)

**Reset email sent confirmation:**

![Reset email sent](docs/testing/passwords/password-reset-email-sent.PNG)

**Set new password:**

![Set new password](docs/testing/passwords/password-enter-new.PNG)

**Password reset complete:**

![Password reset complete](docs/testing/passwords/password-reset-complete.PNG)

## SEO

### Sitemap

![Sitemap](docs/testing/seo/sitemap-xml.png)

### Robots.txt

![Robots.txt](docs/testing/seo/screenshot-robots-txt.png)


## HTML Validation

All pages were validated using the [W3C HTML Validator](https://validator.w3.org/).

| Template | Method | Result |
|----------|--------|--------|
| index.html | URL | ✅ No errors or warnings |
| login.html | URL | ✅ No errors or warnings |
| signup.html | URL | ✅ No errors or warnings |
| password_reset.html | URL | ✅ No errors or warnings |
| password_reset_done.html | Direct input | ✅ No errors or warnings |
| password_reset_from_key.html | Direct input | ⚠️ 4 errors from allauth internal template rendering — not attributable to project code |
| password_reset_from_key_done.html | Direct input | ✅ No errors or warnings |
| profile_detail.html | Direct input | ✅ No errors or warnings |
| create_profile.html | Direct input | ✅ No errors or warnings |
| profile_edit.html | Direct input | ✅ No errors or warnings |
| matches.html | Direct input | ✅ No errors or warnings |
| profile_view.html | Direct input | ✅ No errors or warnings |
| inbox.html | Direct input | ✅ No errors or warnings |
| conversation.html | Direct input | ✅ No errors or warnings |
| 404.html | Direct input | ✅ No errors or warnings |

![index.html validation](docs/testing/validation/html/screenshot-landing-page.png)

![login.html validation](docs/testing/validation/html/screenshot-login-page.png)

![signup.html validation](docs/testing/validation/html/screenshot-signup-page.png)

![password_reset.html validation](docs/testing/validation/html/screenshot-password-reset.png)

![password_reset_done.html validation](docs/testing/validation/html/screenshot-password-reset-done.png)

![password_reset_from_key.html validation](docs/testing/validation/html/screenshot-password-reset-from-key.png)

![password_reset_from_key_done.html validation](docs/testing/validation/html/screenshot-password-reset-complete.png)

![profile_detail.html validation](docs/testing/validation/html/screenshot-profile-detail.png)

![create_profile.html validation](docs/testing/validation/html/screenshot-create-profile.png)

![profile_edit.html validation](docs/testing/validation/html/screenshot-profile-edit.png)

![matches.html validation](docs/testing/validation/html/screenshot-matches.png)

![profile_view.html validation](docs/testing/validation/html/screenshot-profile-view.png)

![inbox.html validation](docs/testing/validation/html/screenshot-inbox.png)

![conversation.html validation](docs/testing/validation/html/screenshot-conversation.png)

![404.html validation](docs/testing/validation/html/screenshot-404.png)

## CSS Validation

`base.css` was validated using the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

| File | Result |
|------|--------|
| base.css | ✅ No errors (54 warnings — vendor prefixes) |

![base.css validation](docs/testing/validation/css/screenshot-css-validation.png)

## Python Validation

All Python files were validated using the [CI Python Linter](https://pep8ci.herokuapp.com/).

| File | Result |
|------|--------|
| accounts/views.py | ✅ No errors |
| accounts/models.py | ✅ No errors |
| accounts/context_processors.py | ✅ No errors |
| matching/views.py | ✅ No errors |
| matching/models.py | ✅ No errors |
| matching/algorithm.py | ✅ No errors |
| matching/tests.py | ✅ No errors |
| profiles/views.py | ✅ No errors |
| profiles/models.py | ✅ No errors |
| profiles/forms.py | ✅ No errors |
| subscriptions/views.py | ✅ No errors |
| subscriptions/models.py | ✅ No errors |
| subscriptions/decorators.py | ✅ No errors |
| sakina/settings.py | ✅ No errors |

![accounts/views.py validation](docs/testing/validation/python/accounts-views.png)

![accounts/models.py validation](docs/testing/validation/python/accounts-models.png)

![accounts/context_processors.py validation](docs/testing/validation/python/accounts-context-processors.png)

![matching/views.py validation](docs/testing/validation/python/matching-views.png)

![matching/models.py validation](docs/testing/validation/python/matching-models.png)

![matching/algorithm.py validation](docs/testing/validation/python/matching-algorithm.png)

![matching/tests.py validation](docs/testing/validation/python/matching-tests.png)

![profiles/views.py validation](docs/testing/validation/python/profiles-views.png)

![profiles/models.py validation](docs/testing/validation/python/profiles-models.png)

![profiles/forms.py validation](docs/testing/validation/python/profiles-forms.png)

![subscriptions/views.py validation](docs/testing/validation/python/subscriptions-views.png)

![subscriptions/models.py validation](docs/testing/validation/python/subscriptions-models.png)

![subscriptions/decorators.py validation](docs/testing/validation/python/subscriptions-decorators.png)

![sakina/settings.py validation](docs/testing/validation/python/sakina-settings.png)

## JavaScript Validation

No custom JavaScript was written for this project. The Stripe checkout redirect is handled server-side in `subscriptions/views.py`. The EmailOctopus newsletter script in the footer is third-party code and not subject to validation.


## Bugs

### Fixed Bugs

#### 500 Error on Matches Page for Users Without a Completed Profile

**Problem:** A user who had paid for a subscription but not yet completed their profile would encounter a 500 server error when clicking the Matches or Profile View links in the navbar. This occurred because the matching views called `request.user.profile` directly, which raises a `RelatedObjectDoesNotExist` exception if no Profile object exists for that user.

**Fix:** A `hasattr` guard was added to the `matches`, `profile_view`, and `refresh_matches` views in `matching/views.py`. If no profile exists, the user is redirected to the Create Profile page instead of the view attempting to access a non-existent object.

```python
if not hasattr(request.user, 'profile'):
    return redirect('profile_create')
```

#### Variable Name Collision Between Django Messages Framework and Inbox/Conversation Views

**Problem:** The inbox and conversation views originally used `messages` as the variable name for queried `Message` objects. This conflicted with Django's built-in `messages` framework, causing the flash message system to break silently across the site.

**Fix:** The query variables were renamed to `inbox_messages` and `conversation_messages` respectively, and the templates updated to match.

#### Profile Photo File Extension Casing on GitHub

**Problem:** Profile photos uploaded with `.PNG` (uppercase) extensions would not render on the deployed site or in the GitHub README, as Linux-based systems treat file extensions as case-sensitive.

**Fix:** Affected files were renamed using `git mv` to enforce lowercase `.png` extensions, and re-committed to ensure GitHub tracked the rename correctly.

#### Signup Form HTML Validation Errors from Allauth Field Rendering

**Problem:** The `signup.html` template produced W3C validation errors because django-allauth's default `{{ form.as_p }}` rendering wrapped `<ul>` elements inside `<span>` elements inside `<p>` elements, which is invalid HTML.

**Fix:** The form was converted from `{{ form.as_p }}` to manual field-by-field rendering, giving full control over the HTML structure and eliminating the validation errors.

### Known Bugs

- The `password_reset_from_key.html` template produces 4 HTML validation errors. These originate from django-allauth's internal template rendering and are not attributable to project code. No fix is possible without overriding allauth's core behaviour.

## Deployment

### Heroku

Sakina is deployed on Heroku at [sakina-matchmaking-7bcbb6fbb05b.herokuapp.com](https://sakina-matchmaking-7bcbb6fbb05b.herokuapp.com/).

#### Steps to deploy

1. Create a new Heroku app
2. Connect the GitHub repository under the Deploy tab
3. Add the following config vars under Settings:
   - `SECRET_KEY`
   - `DATABASE_URL`
   - `STRIPE_PUBLIC_KEY`
   - `STRIPE_SECRET_KEY`
   - `STRIPE_WH_SECRET`
   - `STRIPE_PRICE_ID`
   - `EMAIL_HOST_USER`
   - `EMAIL_HOST_PASS`
   - `USE_AWS`
   - `AWS_STORAGE_BUCKET_NAME`
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
4. Enable automatic deploys from the `main` branch
5. Run migrations: `python manage.py migrate`
6. Seed profiles: `python manage.py seed_profiles`
7. Run matching algorithm: `python manage.py run_matching`

### Local Development

#### Prerequisites
- Python 3.12
- PostgreSQL

#### Setup

1. Clone the repository:
```bash
   git clone https://github.com/Sascha-netizen/sakina_matchmaking
```
2. Create and activate a virtual environment:
```bash
   python -m venv .venv
   .venv\Scripts\activate
```
3. Install dependencies:
```bash
   pip install -r requirements.txt
```
4. Create an `env.py` file in the root directory with the following variables:
```python
   import os
   os.environ["SECRET_KEY"] = "your-secret-key"
   os.environ["DATABASE_URL"] = "your-database-url"
   os.environ["STRIPE_PUBLIC_KEY"] = "your-stripe-public-key"
   os.environ["STRIPE_SECRET_KEY"] = "your-stripe-secret-key"
   os.environ["STRIPE_WH_SECRET"] = "your-stripe-webhook-secret"
   os.environ["STRIPE_PRICE_ID"] = "your-stripe-price-id"
```
5. Run migrations:
```bash
   python manage.py migrate
```
6. Seed profiles:
```bash
   python manage.py seed_profiles
```
7. Run the matching algorithm:
```bash
   python manage.py run_matching
```
8. Start the development server:
```bash
   python manage.py runserver
```


## Test Accounts

The following accounts are available for assessment purposes.

### Superuser

| Field | Value |
|-------|-------|
| Username | Rasheed |
| Email | sascha.r.klement@gmail.com |
| Password | 1Hundchen |

### Test User — Female Profile

| Field | Value |
|-------|-------|
| Username | rania_hassan |
| Email | sascha.r.klement+female@gmail.com |
| Password | 3Hundchen |

### Test User — Male Profile

| Field | Value |
|-------|-------|
| Username | youssef_ali |
| Email | sascha.r.klement+male@gmail.com |
| Password | 2Hundchen |

Both test users are active subscribers with completed profiles and a compatibility score of 82%. Log in as either to view matches, browse profiles, and test the messaging system.

## Future Features

### Real-Time Messaging with WebSockets

The current messaging system uses standard HTTP requests. A future version would implement WebSockets via Django Channels, enabling real-time conversation updates without page refresh — a natural evolution of the platform's direct messaging feature that was descoped to keep the current implementation appropriately sized.

### Wali Notification System

Users who indicate a wali preference could have a dedicated contact flow allowing a guardian to be notified or included in early-stage communication, reflecting the role of the wali in traditional Islamic marriage practice.

### Profile Verification

A verification badge system for users who submit identity or background documentation, increasing trust between members and reducing the risk of misrepresentation.

### Advanced Match Filtering

Expanded filtering on the matches page by religiosity level, marital status, and education, giving subscribers finer control over the profiles they are shown.

### Mobile App

A React Native mobile application to complement the web platform, allowing users to manage their profile and messages on the go.


## Credits

### Code

- [Code Institute Boutique Ado walkthrough](https://github.com/Code-Institute-Solutions/boutique_ado_v1) — structural reference for e-commerce patterns, Stripe integration, and deployment configuration

### Media

- Profile photos sourced from [Pexels](https://www.pexels.com/), [randomuser.me](https://randomuser.me/), and [thispersondoesnotexist.com](https://thispersondoesnotexist.com/)
- Seeded profile data generated using [Faker](https://faker.readthedocs.io/)

### Acknowledgements

- **Tim** (Code Institute mentor) — for guidance and feedback throughout the project
- **Abeer ElAshry** — for discussions about the platform concept and target audience
