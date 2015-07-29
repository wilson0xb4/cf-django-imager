# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_published', models.DateField(auto_now_add=True)),
                ('published', models.CharField(default=b'private', max_length=200, choices=[(b'private', b'private'), (b'shared', b'shared'), (b'public', b'public')])),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'photo_files/%Y-%m-%d')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('date_uploaded', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_published', models.DateField(null=True, blank=True)),
                ('published', models.CharField(default=b'private', max_length=200, choices=[(b'private', b'private'), (b'shared', b'shared'), (b'public', b'public')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(related_name='albums', to='imager_images.Photo'),
        ),
        migrations.AddField(
            model_name='album',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
