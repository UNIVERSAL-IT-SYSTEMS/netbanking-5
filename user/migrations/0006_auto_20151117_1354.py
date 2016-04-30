# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20151117_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='acc_no',
            field=models.BigIntegerField(validators=[django.core.validators.MaxValueValidator(999999999999999), django.core.validators.MinValueValidator(99999999999999)], unique=True, default=0),
        ),
    ]
