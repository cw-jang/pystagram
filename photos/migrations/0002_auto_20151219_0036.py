# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='description',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='image',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='user',
        ),
        migrations.AddField(
            model_name='photo',
            name='image_url',
            field=models.CharField(max_length=512, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='thumb_url',
            field=models.CharField(max_length=512, default=''),
            preserve_default=False,
        ),
    ]
