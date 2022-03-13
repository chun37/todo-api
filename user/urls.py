from django.urls import path

from user.views import CreateUser

urlpatterns = [path("register/", CreateUser.as_view())]
