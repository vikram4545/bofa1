from django.db import models
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
class Employer(models.Model):
    employeId=models.CharField(max_length=20)

class Number(models.Model):
    Driverlicence= 'Driver_Licence'
    PassPort = 'Passport'
    ID_Proof= (
        (Driverlicence, 'Driverlicence'),
        (PassPort, 'PassPort'),
    )
    anumber=models.CharField(max_length=12,default = 0)
    name=models.CharField(max_length=20)
    balance=models.FloatField(default=0)
    identityPr = models.CharField(choices=ID_Proof,default='DL',max_length=15)
    upload = models.FileField(default= None)
    adressp = models.FileField(default= None)
    address= models.TextField(max_length=5000)
    date= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.anumber
class Holder(models.Model):
    #number=models.ForeignKey(Number,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)
    balance=models.FloatField(default=0)
    number=models.CharField(max_length=12)
    name=models.CharField(max_length=20)
    deposite=models.FloatField(default=0)
    withdraw=models.FloatField(default=0)
    def __str__(self):
        return self.name
class Number1(models.Model):
    anumber= models.ForeignKey(Number,on_delete= models.CASCADE)
