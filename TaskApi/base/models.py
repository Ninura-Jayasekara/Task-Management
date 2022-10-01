from enum import auto
from msilib.schema import Class
from django.db import models


class Task(models.Model):
    taskName = models.CharField(max_length = 100)
    description = models.CharField(max_length = 300)
    start = models.DateTimeField(auto_now_add = True)
    due = models.DateTimeField(auto_now_add = False)

