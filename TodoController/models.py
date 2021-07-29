from django.db import models

# Create your models here.
class Todoitem(models.Model):
    item=models.CharField(max_length=255)