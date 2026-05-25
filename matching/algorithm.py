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