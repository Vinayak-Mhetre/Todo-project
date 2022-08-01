from django.db import models

from datetime import datetime
# Create your models here.


class Task(models.Model):
    content = models.CharField(max_length=50)
    date_created = models.DateTimeField(default=datetime.now())
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.content}'

    class Meta:
        ordering = ['-date_created']