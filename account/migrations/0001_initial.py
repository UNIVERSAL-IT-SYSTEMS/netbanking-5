# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('balance', models.IntegerField(null=True)),
                ('account_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('Amount_used', models.IntegerField(default=0)),
                ('Transfer_by', models.ForeignKey(to='account.Account', related_name='transferBy')),
                ('Transfer_to', models.ForeignKey(blank=True, null=True, to='account.Account', related_name='transferTo')),
            ],
        ),
    ]
