# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImagerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('camera', models.CharField(max_length=200)),
                ('address', models.TextField(max_length=200)),
                ('website', models.URLField()),
                ('photography_type', models.CharField(max_length=200)),
            ],
        ),
    ]
