from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.test import TestCase
import factory
from imager_profile.models import ImagerProfile


# Create your tests here.
class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user{}".format((n)))
    email = factory.Sequence(lambda n: "user{}@example.com".format((n)))


class ProfileTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.build()
        self.user.save()

    def test_profile_auto_creation(self):
        self.assertTrue(ImagerProfile.objects.count() == 1)
