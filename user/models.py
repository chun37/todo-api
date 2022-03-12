from functools import partial
from secrets import token_hex

from django.db import models

# Create your models here.


class User(models.Model):
    id = models.CharField(max_length=255, primary_key=True)  # Discord のアカウント ID
    api_key = models.CharField(max_length=128, default=partial(token_hex, 64))
    is_superuser = models.BooleanField(default=False)
