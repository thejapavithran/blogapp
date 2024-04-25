from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    date_created=models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to='profile')