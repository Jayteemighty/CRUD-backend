from django.db import models

# Create your models here.
class post(models.Model):
    username = models.CharField(max_length=100)
    description = models.CharField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)
