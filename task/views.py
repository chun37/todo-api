from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from task.models import Task
from task.serializers import TaskListSerializer, TaskUpdateStatusSerializer

# Create your views here.


class TaskList(ListCreateAPIView):
    serializer_class = TaskListSerializer

    def get_queryset(self):
        status = self.request.GET.get("status", None)
        if status is None:
            return Task.objects.all()
        return Task.objects.filter(status=status)


class TaskUpdate(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskUpdateStatusSerializer

    def put(self, request, *args, **kwargs):
        instance: Task = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data["status"] <= instance.status:
            raise ValidationError("ステータスは進めることしか出来ません")

        self.perform_update(serializer)

        return Response(serializer.data)
