# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20151117_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='acc_no',
            field=models.BigIntegerField(default=0, unique=True, validators=[django.core.validators.MaxLengthValidator(16), django.core.validators.MinValueValidator(15)]),
        ),
    ]
