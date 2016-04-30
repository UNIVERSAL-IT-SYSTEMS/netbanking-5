# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintainbill', '0002_auto_20151102_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='phone_no',
            field=models.IntegerField(null=True),
        ),
    ]
