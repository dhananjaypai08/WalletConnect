from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=200)
    password = models.TextField(max_length=255)
