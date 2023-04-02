from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError

class Tasks(models.Model):
    def __str__(self):
        return "{}".format(self.name)
        
    name = models.CharField(max_length=300)
    desc = models.CharField(max_length=700, default='')
    start_time_date = models.DateTimeField(null=True)
    end_time_date = models.DateTimeField(null=True)


    def clean(self):
        if self.start_time_date > self.end_time_date:
            raise ValidationError('End time must be after start time.')
        
    