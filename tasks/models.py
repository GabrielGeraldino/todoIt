from django.db import models

# Create your models here.
class Task (models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=45)
    endDate = models.DateField()

    def __str__(self):
        return f"[Task] title: {self.title}"