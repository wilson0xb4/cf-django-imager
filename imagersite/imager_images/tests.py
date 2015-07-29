from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.test import TestCase
import factory

from imager_images.models import Photo, Album


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user{}".format((n)))
    email = factory.Sequence(lambda n: "user{}@example.com".format((n)))


class PhotoFactory(factory.Factory):
    class Meta:
        model = Photo


class AlbumFactory(factory.Factory):
    class Meta:
        model = Album


class PhotoTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.build()
        self.user.save()  # why can't I chain .build().save()?
        self.photo = PhotoFactory.build(user=self.user)

    def test_add_photo(self):
        """Create a new photo."""
        self.assertEqual(Photo.objects.count(), 0)
        self.photo.save()
        self.assertEqual(Photo.objects.count(), 1)

    def test_photo_belongs_to(self):
        """Test if photo belongs to a certain user."""
        self.assertTrue(self.photo.user)

    def test_photo_does_not_belong_to(self):
        """Test if photo does not belong to a certain user."""
        self.assertIsNot(self.photo.user, UserFactory.build())


class AlbumTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.build()
        self.user.save()
        self.album = AlbumFactory.build(user=self.user)

    def test_add_album(self):
        """Create a new album."""
        self.assertEqual(Album.objects.count(), 0)
        self.album.save()
        self.assertEqual(Album.objects.count(), 1)

    def test_album_belongs_to(self):
        """Test if album belongs to user."""
        self.assertTrue(self.album.user)

    def test_album_does_not_belong_to(self):
        """Test if album does not belong to user."""
        self.assertIsNot(self.album.user, UserFactory.build())

    def test_add_photo_to_album(self):
        """Verify empty album, add photo, check count."""
        self.album.save()
        self.assertEqual(self.album.photos.count(), 0)
        photo = PhotoFactory.build(user=self.user)
        photo.save()
        self.album.photos.add(photo)
        self.assertEqual(self.album.photos.count(), 1)
