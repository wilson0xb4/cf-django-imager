# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.TextField(help_text=b'Enter a description for your photo album.', blank=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(help_text=b'Enter a title for your photo album.', max_length=200),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(help_text=b'Enter a description of your photo.', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(help_text=b'Enter a title for your photo.', max_length=200),
        ),
    ]
