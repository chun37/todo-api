# Generated by Django 4.0.3 on 2022-03-12 12:26

import functools
import secrets

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('api_key', models.CharField(default=functools.partial(secrets.token_hex, *(64,), **{}), max_length=128)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
        ),
    ]
