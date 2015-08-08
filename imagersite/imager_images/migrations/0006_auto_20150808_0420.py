# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0005_auto_20150805_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='published',
            field=models.CharField(default='private', max_length=7, choices=[('private', 'private'), ('shared', 'shared'), ('public', 'public')]),
        ),
        migrations.AlterField(
            model_name='photo',
            name='published',
            field=models.CharField(default='private', max_length=7, choices=[('private', 'private'), ('shared', 'shared'), ('public', 'public')]),
        ),
    ]
