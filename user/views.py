from django.contrib.auth import get_user_model
from django.http.request import HttpRequest
from django.shortcuts import render
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import CreateAPIView

from user.serializers import CreateUserSerializer

# Create your views here.


class CreateUser(CreateAPIView):
    serializer_class = CreateUserSerializer

    def create(self, request: HttpRequest, *args, **kwargs):
        # is_admin か確認する。違う場合は status_code: 403
        if not request.user.is_admin:
            raise PermissionDenied

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()

        # 送られてきた id が存在する場合は削除する
        User = get_user_model()
        try:
            created_user = User.objects.get(id=request.data["id"])
            created_user.delete()
        except User.DoesNotExist:
            pass  # 存在しなければ何もしないので握りつぶす

        return super().create(request, *args, **kwargs)
