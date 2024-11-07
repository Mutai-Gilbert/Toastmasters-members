from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    club = models.CharField(max_length=200)
    club_email = models.EmailField()
    club_phone = models.CharField(max_length=200)
    club_address = models.CharField(max_length=200)
    club_city = models.CharField(max_length=200)
    club_state = models.CharField(max_length=200)
    club_zipcode = models.CharField(max_length=200)
