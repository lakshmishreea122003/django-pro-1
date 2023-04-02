from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Task(models.Model):
    def __str__(self):
        return "{}".format(self.name)
        
    name=models.CharField(max_length=300)

