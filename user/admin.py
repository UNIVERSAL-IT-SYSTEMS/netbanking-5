from django.contrib import admin
from user.models import MyUser
from account.models import Account,Transaction
# Register your models here.
admin.site.register(MyUser);
admin.site.register(Account);
admin.site.register(Transaction);
