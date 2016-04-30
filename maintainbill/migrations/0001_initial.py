# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date_of_payment', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField(null=True)),
                ('bill_status', models.CharField(choices=[('unpaid', 'not_paid'), ('paid', 'paid')], default='unpaid', max_length=6)),
                ('amount', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('phone_no', models.IntegerField()),
                ('customer_id', models.CharField(max_length=10, unique=True)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_address', models.CharField(max_length=1000)),
            ],
        ),
    ]
