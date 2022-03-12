from django.urls import path

from task.views import TaskList

urlpatterns = [path("", TaskList.as_view())]
