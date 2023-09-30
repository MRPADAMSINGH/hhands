from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import os

# Create your models here.
class CustomUser(AbstractUser):

    STATUS = (
        ('regular', 'regular'),
        ('subscriber', 'subscriber'),
        ('moderator', 'moderator'),
    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='regular')
    description = models.TextField("Description", max_length=600, default='', blank=True)

    def __str__(self):
        return self.username


class Contact(models.Model):
    firstname = models.CharField(max_length=122)
    lastname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.firstname
    
class Join_us(models.Model):
    name = models.CharField(max_length=122)
    state = models.CharField(max_length=122)
    mobile = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    transaction = models.CharField(max_length=122)
    message = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    mobile = models.CharField(max_length=122)
    stuclass = models.CharField(max_length=122)
    aadharcard = models.CharField(max_length=122)
    dob = models.CharField(max_length=122)
    address = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.name



class SubscribedUsers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email