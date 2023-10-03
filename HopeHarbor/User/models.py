from django.db import models

# Create your models here.
class User(models.Model):
    UserID = models.BigAutoField(primary_key = True)
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    EmailAddress = models.EmailField()
    Password = models.CharField(max_length=20)
    UserType = (('donor', 'donor'), ('beneficiary', 'beneficiary'), ('admin', 'admin'))
    pass

#Gian