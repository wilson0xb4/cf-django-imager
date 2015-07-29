from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.test import TestCase
import factory

from imager_profile.models import ImagerProfile


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user{}".format((n)))
    email = factory.Sequence(lambda n: "user{}@example.com".format((n)))


class ProfileTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.build()

    def test_profile_auto_creation(self):
        """If user is created, ImagerProfile should be too."""
        self.assertTrue(ImagerProfile.objects.count() == 0)
        self.user.save()
        self.assertTrue(ImagerProfile.objects.count() == 1)

    def test_profile_auto_delete(self):
        """If user is deleted, ImagerProfile should be too."""
        self.user.save()
        self.assertTrue(ImagerProfile.objects.count() == 1)
        self.user.delete()
        self.assertTrue(ImagerProfile.objects.count() == 0)

    def test_user_auto_delete(self):
        """If ImagerProfile is deleted, User should be too."""
        self.user.save()
        self.assertTrue(User.objects.count() == 1)
        self.user.profile.delete()
        self.assertTrue(User.objects.count() == 0)

    def test_profile_camera(self):
        self.user.save()
        self.assertEqual(self.user.profile.camera, '')
        self.user.profile.camera = 'Leica'
        self.assertEqual(self.user.profile.camera, 'Leica')

    def test_profile_address(self):
        self.user.save()
        self.assertEqual(self.user.profile.address, '')
        self.user.profile.address = '511 Boren Avenue North'
        self.assertEqual(self.user.profile.address, '511 Boren Avenue North')

    def test_profile_website(self):
        self.user.save()
        self.assertEqual(self.user.profile.website, '')
        self.user.profile.website = 'example.com'
        self.assertEqual(self.user.profile.website, 'example.com')

    def test_profile_photo_type(self):
        self.user.save()
        self.assertEqual(self.user.profile.photography_type, '')
        self.user.profile.photography_type = 'Landscape'
        self.assertEqual(self.user.profile.photography_type, 'Landscape')

    def test_is_active(self):
        self.user.save()
        self.assertTrue(self.user.profile.is_active())
