# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0002_auto_20150727_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='address',
            field=models.TextField(help_text=b'What is your address?', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='camera',
            field=models.CharField(help_text=b'What is your favorite camera?', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='photography_type',
            field=models.CharField(help_text=b'What type of photographer are you?', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='website',
            field=models.URLField(help_text=b'What is your website URL?', blank=True),
        ),
    ]
