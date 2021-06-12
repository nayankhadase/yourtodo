from django.db import models

# Create your models here.
class Task(models.Model):
    user_data=models.CharField(default='none',max_length=100)
    task=models.CharField(max_length=100)