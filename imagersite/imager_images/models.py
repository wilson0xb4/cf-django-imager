from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

PUBLISHED_CHOICES = (
    ('private', 'private'),
    ('shared', 'shared'),
    ('public', 'public')
)


@python_2_unicode_compatible
class Photo(models.Model):
    user = models.ForeignKey(
        User,
        null=False
    )
    image = models.ImageField(
        upload_to='photo_files/%Y-%m-%d'
    )
    title = models.CharField(
        max_length=200,
        help_text='Enter a title for your photo.'
    )
    description = models.TextField(
        blank=True,
        help_text='Enter a description of your photo.'
    )
    date_uploaded = models.DateField(
        auto_now_add=True
    )
    date_modified = models.DateField(
        auto_now=True
    )
    date_published = models.DateField(
        null=True,
        blank=True
    )
    published = models.CharField(
        max_length=200,
        choices=PUBLISHED_CHOICES,
        default='private'
    )

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Album(models.Model):
    user = models.ForeignKey(
        User,
        null=False
    )
    photos = models.ManyToManyField(
        Photo,
        related_name='albums',
        blank=True,
    )
    title = models.CharField(
        max_length=200,
        help_text='Enter a title for your photo album.'
    )
    description = models.TextField(
        blank=True,
        help_text='Enter a description for your photo album.'
    )
    cover = models.ForeignKey(
        Photo,
        related_name='cover_to',
        null=True,
        blank=True
    )
    date_created = models.DateField(
        auto_now_add=True
    )
    date_modified = models.DateField(
        auto_now=True
    )
    date_published = models.DateField(
        auto_now_add=True
    )
    published = models.CharField(
        max_length=200,
        choices=PUBLISHED_CHOICES,
        default='private'
    )

    def __str__(self):
        return self.title
