from django.db import models

# Create your models here.

class Reciepe(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.TextField()
    Image = models.ImageField(upload_to="reciepe")