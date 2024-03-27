from django.db import models
import uuid

# Create your models here.
class blogs(models.Model):
    Title = models.CharField(max_length=100, null=True, blank=True)
    Desc= models.CharField(max_length = 3000, null=True, blank=True)
    id = models.IntegerField(primary_key=True, editable=False)
    def __str__(self):
        return self.Title