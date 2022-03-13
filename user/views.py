from typing import Optional

from django.shortcuts import render
from django.http.request import HttpRequest
from rest_framework.generics import CreateAPIView
from rest_framework.exceptions import NotAuthenticated, PermissionDenied

from user.serializers import CreateUserSerializer
from user.models import User

# Create your views here.


class CreateUser(CreateAPIView):
    serializer_class = CreateUserSerializer

    def create(self, request: HttpRequest, *args, **kwargs):
        # header の Authorization を読み、api_key を取得する。Authorization が存在しない 又は 値が空文字 の場合は status_code: 401
        api_key: Optional[str] = request.headers.get("Authorization", None)
        if api_key is None or api_key == "":
            raise NotAuthenticated

        # api_key を元に、User を取ってくる。存在しない場合は status_code: 401
        try:
            accessed_user = User.objects.get(api_key=api_key)
        except ObjectDoesNotExist:
            return NotAuthenticated

        # accessed_user を元に is_superuser か確認する。違う場合は status_code: 403
        if not accessed_user.is_superuser:
            return PermissionDenied

        # 送られてきた id が存在する場合は削除する
        if user_id := request.data.get("id", ""):
            try:
                created_user = User.objects.get(id=user_id)
                created_user.delete()
            except ObjectDoesNotExist:
                pass  # 存在しなければ何もしないので握りつぶす

        return super().create(request, *args, **kwargs)
