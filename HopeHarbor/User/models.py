from django.db import models

# Create your models here.
class User(models.Model):
    UserID = models.BigAutoField(primary_key = True)
    FirstName = models.CharField()
    LastName = models.CharField()
    EmailAddress = models.EmailField()
    Password = models.CharField()
    UserType = (('donor', 'donor'), ('beneficiary', 'beneficiary'), ('admin', 'admin'))
    pass

#Gian