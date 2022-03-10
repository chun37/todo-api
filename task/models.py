from django.db import models
from task.enums import TaskStatus
import uuid

# Create your models here.


class Task(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    content = models.CharField(max_length=4000)  # NOTE: Discord のメッセージの最大文字数が 4000
    status = models.IntegerField(
        choices=TaskStatus.choices, default=TaskStatus.WORKING_ON, editable=False
    )
    updated_at = models.DateTimeField(auto_now=True, editable=False)
