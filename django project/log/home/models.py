from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField( max_length=150)
    phone = models.CharField(max_length=150)
    date = models.DateField()