from rest_framework import serializers

from task.models import Task


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "content", "status", "updated_at")
        read_only_fields = ("id", "status", "updated_at")
