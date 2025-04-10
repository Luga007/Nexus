from django.test import TestCase
from user.models import Profile

class TestProfile(TestCase):
    def test_profile(self):
        profile = Profile.objects.create(firstname='John', last_name='Smith', phone_number='555-555-5555', bio='Sure')
        self.assertEqual(profile.firstname, 'John')
        self.assertEqual(profile.last_name, 'Smith')
        self.assertEqual(profile.phone_number, '555-555-5555')
        self.assertEqual(profile.bio, 'Sure')