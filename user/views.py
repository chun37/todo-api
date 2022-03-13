from typing import Optional

from django.http.request import HttpRequest
from django.shortcuts import render
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import CreateAPIView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist

from user.models import User
from user.serializers import CreateUserSerializer

# Create your views here.


class CreateUser(CreateAPIView):
    serializer_class = CreateUserSerializer

    def create(self, request: HttpRequest, *args, **kwargs):
        # accessed_user を元に is_superuser か確認する。違う場合は status_code: 403
        if not request.accessed_user.is_superuser:
            raise PermissionDenied

        # 送られてきた id が存在する場合は削除する
        if user_id := request.data.get("id", ""):
            try:
                created_user = User.objects.get(id=user_id)
                created_user.delete()
            except ObjectDoesNotExist:
                pass  # 存在しなければ何もしないので握りつぶす

        return super().create(request, *args, **kwargs)
