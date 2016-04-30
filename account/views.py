from django.shortcuts import render
from django.core.urlresolvers import reverse
# Create your views here.
from django.shortcuts import get_object_or_404,redirect,render
from user.models import MyUser
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods,require_GET,require_POST
from django.contrib.auth.decorators import login_required
from .models import Account,Transaction
from django.contrib.auth import login,logout,authenticate
from .forms import *
from maintainbill.models import *
# Create your views here.
@require_GET
@login_required

def balEnquiry(request):
	id=request.user.id
	customer=get_object_or_404(NewUser,id=id)
	balance=customer.account.balance
	data={'customer':customer,'balance':balance}
	return render(request,'showBalance.html',data)
@require_GET
def base(request):
	if request.user.is_authenticated():
		for checkuser in MyUser.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'main.html')
		return render(request,'mainservice.html')
	else:
		return render(request,'base.html')
@require_GET
@login_required
def transDetails(request):
	id=request.user.id
	customer=get_object_or_404(NewUser,id=id)
	transbyu=Transaction.objects.filter(Transfer_by=customer.account)
	transtou=Transaction.objects.filter(Transfer_to=customer.account)
	data={'user':customer,'transbyu':transbyu,'transtou':transtou}
	return render(request,'showTransactions.html',data)
@require_GET
@login_required
def changeBalance(request,bal):
	for checkuser in ServiceProvider.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginuser.html')
	id=request.user.id
	customer=get_object_or_404(MyUser,id=id)
	balance=customer.account.balance
	
	if balance>bal:
		new_bal=balance-bal
		balance=new_bal
		customer.account.save()
		data={'confirmed':True}
		return render(request,'main.html',data)
	else:
		data={'confirmed':False}
		return render(request,'incompletetransaction.html',data)
@require_GET
@login_required
def Transfer(request):
	for checkuser in ServiceProvider.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginuser.html')
	transferform=TransferForm()
	data={'transferform':transferform}
	return render(request,'transfer.html',data)
@require_POST
@login_required
def handleTransfer(request):
	for checkuser in ServiceProvider.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginuser.html')
	user=request.user
	f=TransferForm(request.POST)
	if f.is_valid():		
		transfer_to=f.cleaned_data['Transfer_to']
		Amount_used=f.cleaned_data['Amount_used']
	if user.account.balance>Amount_used:
		user.account.balance=user.account.balance-Amount_used
		transfer_to.balance=transfer_to.balance+Amount_used
		q=Transaction(Transfer_by=user.account,Amount_used=Amount_used,Transfer_to=transfer_to)
		q.save();
		transfer_to.save()
		user.account.save()
		data={'confirmed':True,'t':transfer_to.balance}
		return render(request,'main.html',data)
	else:
		return render(request,'incompletetransaction.html')





	
