from django.db import models


class Student(models.Model):
    s_name = models.CharField(max_length=32),
    s_class = models.CharField(max_length=16),
