from django.db import models
from user.models import NewUser
from django.core.validators import MaxValueValidator,MinValueValidator
class Account(models.Model):
  account_holder=models.OneToOneField(NewUser)
  balance = models.IntegerField(default=0,null=True)
  account_number=models.BigIntegerField(validators=[MaxValueValidator(999999999999999) , MinValueValidator(99999999999999),],blank=False,default=0,unique=True)
  def __str__(self):
    return str(self.account_number)

class Transaction(models.Model):
  Transfer_by=models.ForeignKey(Account,related_name="transferBy")
  date=models.DateTimeField(auto_now_add=True)
  Amount_used=models.IntegerField(blank=False,default=0)
  Transfer_to=models.ForeignKey(Account,related_name="transferTo",blank=True,null=True)
  def __str__(self):
    sec=""
    if self.Transfer_to :
      sec=str(self.Transfer_to.account_number)
    else:
      sec="some other type"
    return u'%s -----------> %s' % (str(self.Transfer_by.account_number),sec)
  
