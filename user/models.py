from functools import partial
from secrets import token_hex

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, id, password=None):
        if not id:
            raise ValueError("User must have an id")

        user = self.model(
            id=id,
        )
        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, id, password):
        user = self.create_user(
            id=id,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(max_length=255, primary_key=True)  # Discord のアカウント ID
    api_key = models.CharField(max_length=128, default=partial(token_hex, 64))
    is_admin = models.BooleanField(default=False)
    password = models.CharField(_("password"), max_length=128, null=True, blank=True)

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    objects = UserManager()

    USERNAME_FIELD = "id"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.id
