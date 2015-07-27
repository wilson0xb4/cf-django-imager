from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class ActiveProfileManager(models.Manager):
    def get_queryset(self):
        return super(ActiveProfileManager, self).get_queryset().filter(
            user__is_active=True
        )


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        null=False
    )
    camera = models.CharField(
        max_length=200,
        help_text='What is your favorite camera?'
    )
    address = models.TextField(
        max_length=200,
        help_text='What is your address?'
    )
    website = models.URLField(
        help_text='What is your website URL?'
    )
    photography_type = models.CharField(
        max_length=200,
        help_text='What type of photographer are you?'
    )

    objects = models.Manager()
    active = ActiveProfileManager()

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    def is_active(self):
        return self.user.is_active
