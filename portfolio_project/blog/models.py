from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)    
    body = models.TextField(editable=True)
    date = models.DateTimeField(auto_now_add=True)
    url = models.URLField(blank=True)