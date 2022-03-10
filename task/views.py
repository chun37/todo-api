from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from task.models import Task
from task.serializers import TaskListSerializer

# Create your views here.


class TaskList(ListCreateAPIView):
    serializer_class = TaskListSerializer

    def get_queryset(self):
        status = self.request.GET.get("status", 0)
        return Task.objects.filter(status=status)
