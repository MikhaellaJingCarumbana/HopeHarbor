from django.db import models
from User.models import User
# Create your models here.
class Beneficiary(User):
    BeneficiaryID = models.BigAutoField(primary_key = True)
    Needs = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    pass

#Jing