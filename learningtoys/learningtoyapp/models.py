from django.db import models

class contact(models.Model):
    firstname = models.CharField(max_length=255) 
    lastname  = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    subject = models.CharField(max_length=255)
    message = models.TextField()