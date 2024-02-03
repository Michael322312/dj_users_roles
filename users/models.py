from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.ManyToManyField("Role", related_name="roles")

class Role(models.Model):
    name = models.CharField(max_length=100)
