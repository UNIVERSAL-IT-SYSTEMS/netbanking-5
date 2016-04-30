from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator,MinLengthValidator,MaxLengthValidator
import datetime
# Create your models here.
class NewUser(AbstractUser):
  phone=models.BigIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(999999999),],blank=False,default=0)
  acc_no=models.BigIntegerField(validators=[MaxValueValidator(999999999999999),MinValueValidator(99999999999999),],blank=False,default=0,unique=True)
  address=models.CharField(max_length=200)
  #class Meta:
    #abstract=True
 #def __str__(self): 
 #return self.name
class MyUser(NewUser):
  dob=models.DateField(blank=False,default=datetime.date.today)
  father_name=models.CharField(max_length=50,validators=[MinLengthValidator(6),])
  beneficiary=models.ManyToManyField("self",symmetrical=False,related_name="benefic",blank=True,null=True)
  signature=models.ImageField(blank=True,null=True,upload_to="upload/")
