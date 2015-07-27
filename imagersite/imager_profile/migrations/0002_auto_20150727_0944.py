# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imager_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagerprofile',
            name='user',
            field=models.OneToOneField(related_name='profile', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='address',
            field=models.TextField(help_text=b'What is your address?', max_length=200),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='camera',
            field=models.CharField(help_text=b'What is your favorite camera?', max_length=200),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='photography_type',
            field=models.CharField(help_text=b'What type of photographer are you?', max_length=200),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='website',
            field=models.URLField(help_text=b'What is your website URL?'),
        ),
    ]
