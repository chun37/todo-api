from django.urls import path

from task.views import TaskList, TaskUpdate

urlpatterns = [
    path("", TaskList.as_view()),
    path("<str:pk>/", TaskUpdate.as_view()),
]
