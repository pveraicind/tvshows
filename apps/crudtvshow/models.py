from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField( max_length=50)
    release_date = models.TextField(max_length=50)
    network = models.TextField(max_length=50)
    desc = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)