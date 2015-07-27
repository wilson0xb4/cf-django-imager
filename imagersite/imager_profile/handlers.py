from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import ImagerProfile


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    instance = kwargs.get('instance')
    if not instance or kwargs.get('raw', False):
        return
    try:
        instance.profile
    except ImagerProfile.DoesNotExist:
        instance.profile = ImagerProfile()
        instance.profile.save()


@receiver(post_delete, sender=ImagerProfile)
def delete_user(sender, **kwargs):
    instance = kwargs.get('instance')
    if not instance:
        return
    try:
        instance.user.delete()
    except User.DoesNotExist:
        pass
