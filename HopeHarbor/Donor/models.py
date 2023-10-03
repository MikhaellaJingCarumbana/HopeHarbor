from django.db import models
from User.models import User
# Create your models here.
class Donor(User):
    DonorID = models.BigAutoField(primary_key = True)
    DonationType = (('cash', 'cash'), ('materials', 'materials'))
    pass

class CashDetails(models.Model):
    Amount = models.FloatField()
    Date = models.DateField()
    pass

class GoodsDetail(models.Model):
    Quantity = models.IntegerField()
    Expiry = models.DateField()
    Date = models.DateField()
    pass

class Currency(models.Model):
    CurrencyID = models.BigAutoField(primary_key= True)
    CurrencyType = models.CharField(max_length=20)

class DIK(models.Model):
    DikID = models.BigAutoField(primary_key = True)
    DikType = models.CharField(max_length=20)
    pass

class Amount_Tracker(models.Model):
    Amount = models.FloatField()
    pass

class Goods_Tracker(models.Model):
    Quantity = models.IntegerField()

#Rowen and Gian

