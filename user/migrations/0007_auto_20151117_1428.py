# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20151117_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='signature',
            field=models.ImageField(blank=True, upload_to='upload/', null=True),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='phone',
            field=models.BigIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(999999999)], default=0),
        ),
    ]
