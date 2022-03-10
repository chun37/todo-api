from django.db import models
from django.utils.translation import gettext_lazy as _


class TaskStatus(models.IntegerChoices):
    WORKING_ON = 0, _("作業中")
    COMPLETED = 1, _("完了")
    FAILED = 2, _("失敗")
