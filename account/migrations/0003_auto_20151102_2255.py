# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_account_holder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.BigIntegerField(validators=[django.core.validators.MaxValueValidator(999999999999999), django.core.validators.MinValueValidator(99999999999999)], default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.IntegerField(null=True, default=0),
        ),
    ]
