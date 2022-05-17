from django.db import models

# Create your models here.

class ModelTask(models.Model):
    title_task = models.CharField(max_length=200)
    description_task = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title_task