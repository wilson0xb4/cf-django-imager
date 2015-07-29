# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0002_auto_20150727_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ForeignKey(related_name='cover_to', to='imager_images.Photo', null=True),
        ),
    ]
