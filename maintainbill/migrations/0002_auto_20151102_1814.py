# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('maintainbill', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('newuser_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, serialize=False, auto_created=True, parent_link=True, primary_key=True)),
                ('company_name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            bases=('user.newuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='provider',
            field=models.ForeignKey(to='maintainbill.ServiceProvider', related_name='created'),
        ),
    ]
