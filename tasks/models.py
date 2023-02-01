from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task (models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=45)
    endDate = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f"[Task] title: {self.title}"