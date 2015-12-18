# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20151219_0036'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ForeignKey(default='', to='photos.Photo'),
            # field=models.ForeignKey(null=True, to='photos.Photo'),
            preserve_default=False,
        ),
    ]
