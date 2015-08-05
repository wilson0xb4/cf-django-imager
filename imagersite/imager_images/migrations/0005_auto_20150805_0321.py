# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0004_auto_20150729_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(related_name='albums', to='imager_images.Photo', blank=True),
        ),
    ]
