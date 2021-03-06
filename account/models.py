from django.db import models

# Create your models here.
class Account(models.Model):
    ## Django create unique ID automatically if no specification
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)