from django.shortcuts import render,redirect,get_object_or_404
from maintainbill.models import *
from user.models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods,require_GET,require_POST
from .forms import *
from account.models import *
# Create your views here.

@require_GET
def renderBillPayment(request):
	
	form=BillPayment(request.POST or None,request.FILES or None)
	next_url=request.GET.get('next')
	data={'form':form}
	return render(request,'BillPaymentForm.html',data)

@require_POST
def handleBillPayment(request):
	form=BillPayment(request.POST or None,request.FILES or None)
	next_url=request.GET.get('next')
	data={'form':form,'next':next_url}
	if(form.is_valid()):
		bill=form.save(commit=False)
		bill.save()
		return render(request,'payment.html',{'amount':amount})
	else:
		return render(request,'BillPaymentForm.html',data)



@require_GET
@login_required
def ShowEnterId(request):
	for checkuser in ServiceProvider.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginuser.html')
	form=EnterCustomerId()
	data={'form':form}
	return render(request,'BillPaymentForm.html',data)

@require_POST
@login_required
def ShowPayment(request):
	for checkuser in ServiceProvider.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginuser.html')
	f=EnterCustomerId(request.POST)
	#user=request.user
	if f.is_valid():
		cust_id=f.cleaned_data['customer_id']
		provider=f.cleaned_data['serviceprovider']
		bills=Bill.objects.all()
		x=0
		for sbill in bills:
			if sbill.customer_id==cust_id:
				x=1;
		if x is 1:
			bill=get_object_or_404(Bill,customer_id=cust_id)
			if bill.provider==provider:
				request.session['bill']=cust_id
				data={'bill':bill}
				return render(request,'showbill.html',data)
			else:
				return render(request,'invalidCustomer.html')
		else:
			return render(request,'invalidCustomer.html',{'form':f})
	else:
		return render(request,'BillPaymentForm.html',{'form':f})
	#return render(request,'check.html',data)
@require_POST
@login_required
def renderOtp(request):
	form=EnterOtp()
	request.session['bill']=request.session['bill']
	return render(request,'otp.html',{'form':form})
@require_POST
@login_required
def MakePayment(request):
	for checkuser in ServiceProvider.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginuser.html')
	f=EnterOtp(request.POST)
	if f.is_valid():
		user=request.user
		f="confirmed"
		#bill=request.GET
		cust_id=request.session['bill']
		bill=Bill.objects.get(customer_id=cust_id)
		if user.account.balance>bill.amount:
			user.account.balance=user.account.balance-bill.amount
			bill.provider.account.balance=bill.provider.account.balance+bill.amount
			bill.bill_status=bill.STATUS_CHOICES[1][1]
			q=Transaction(Transfer_by=user.account,Amount_used=bill.amount,Transfer_to=bill.provider.account)
			q.save()	
			user.account.save()
			bill.provider.account.save()
			bill.save()
			data={'f':bill.bill_status}
			return render(request,'main.html',data)
		else:
			return render(request,'incompleteTransaction.html')
	else:
		return render(request,'otp.html',{'form':f})
	

