# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20151117_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='father_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
    ]
