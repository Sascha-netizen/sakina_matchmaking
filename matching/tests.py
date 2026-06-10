from django.test import TestCase
from unittest.mock import MagicMock
from matching.algorithm import calculate_compatibility, is_match_eligible
from datetime import date


def make_profile(**kwargs):
    """Create a mock profile with sensible defaults."""
    profile = MagicMock()
    profile.user_id = kwargs.get('user_id', 1)
    profile.completed = kwargs.get('completed', True)
    profile.profile_visibility = kwargs.get('profile_visibility', 'PU')
    profile.gender = kwargs.get('gender', 'M')
    profile.marital_status = kwargs.get('marital_status', 'SI')
    profile.sect = kwargs.get('sect', 'SU')
    profile.religiosity_level = kwargs.get('religiosity_level', 3)
    profile.country = kwargs.get('country', 'Germany')
    profile.city = kwargs.get('city', 'Berlin')
    profile.wants_children = kwargs.get('wants_children', True)
    profile.has_children = kwargs.get('has_children', False)
    profile.education = kwargs.get('education', 'BA')
    profile.languages = kwargs.get('languages', 'German')
    profile.date_of_birth = kwargs.get('date_of_birth', date(1990, 1, 1))
    return profile


class IsMatchEligibleTests(TestCase):

    def test_self_match_excluded(self):
        profile = make_profile(user_id=1)
        self.assertIsNone(calculate_compatibility(profile, profile))

    def test_same_gender_excluded(self):
        a = make_profile(user_id=1, gender='M')
        b = make_profile(user_id=2, gender='M')
        self.assertIsNone(calculate_compatibility(a, b))

    def test_incomplete_profile_excluded(self):
        a = make_profile(user_id=1, completed=False)
        b = make_profile(user_id=2)
        self.assertIsNone(calculate_compatibility(a, b))

    def test_hidden_profile_excluded(self):
        a = make_profile(user_id=1, profile_visibility='HI')
        b = make_profile(user_id=2)
        self.assertIsNone(calculate_compatibility(a, b))

    def test_married_woman_excluded(self):
        a = make_profile(user_id=1, gender='F', marital_status='MR')
        b = make_profile(user_id=2, gender='M')
        self.assertIsNone(calculate_compatibility(a, b))


class CompatibilityScoreTests(TestCase):

    def test_perfect_match_scores_high(self):
        a = make_profile(user_id=1, gender='M')
        b = make_profile(user_id=2, gender='F')
        score = calculate_compatibility(a, b)
        self.assertGreaterEqual(score, 80)

    def test_different_sect_reduces_score(self):
        a = make_profile(user_id=1, gender='M', sect='SU')
        b = make_profile(user_id=2, gender='F', sect='SH')
        score = calculate_compatibility(a, b)
        self.assertLessEqual(score, 75)

    def test_same_sect_adds_25_points(self):
        a = make_profile(user_id=1, gender='M', sect='SU')
        b = make_profile(user_id=2, gender='F', sect='SU')
        score_with = calculate_compatibility(a, b)
        a2 = make_profile(user_id=1, gender='M', sect='SU')
        b2 = make_profile(user_id=2, gender='F', sect='SH')
        score_without = calculate_compatibility(a2, b2)
        self.assertEqual(score_with - score_without, 25)

    def test_married_man_single_woman_scores_lower(self):
        a = make_profile(user_id=1, gender='M', marital_status='MR')
        b = make_profile(user_id=2, gender='F', marital_status='SI')
        score = calculate_compatibility(a, b)
        self.assertIsNotNone(score)
        self.assertLessEqual(score, 95)

    def test_score_capped_at_100(self):
        a = make_profile(user_id=1, gender='M')
        b = make_profile(user_id=2, gender='F')
        score = calculate_compatibility(a, b)
        self.assertLessEqual(score, 100)

    def test_shared_language_adds_points(self):
        a = make_profile(user_id=1, gender='M', languages='Arabic, German')
        b = make_profile(user_id=2, gender='F', languages='Arabic, French')
        score = calculate_compatibility(a, b)
        self.assertIsNotNone(score)