# Generated by Django 4.0.3 on 2022-03-12 23:26

from django.db import migrations, models
import functools
import secrets


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='api_key',
            field=models.CharField(default=functools.partial(secrets.token_hex, *(64,), **{}), editable=False, max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]