from django.shortcuts import redirect,render,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods,require_GET,require_POST
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from user.models import MyUser
# Create your views here.
@require_GET
@login_required
def renderBillPayment(request):
	form=BillPayment(request.POST or None,request.FILES or None)
	#next_url=request.GET.get('next')
	data={'form':form}
	return render(request,'BillPaymentForm.html',data)
@require_GET
@login_required
def Bills(request):
	for checkuser in MyUser.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginservice.html')
	#next_url=request.GET.get('next')
	bills=get_object_or_404(ServiceProvider,id=request.user.id).created.all()
	data={'bills':bills}
	
	return render(request,'Bills.html',data)
@require_POST
@login_required
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
def renderBillAdd(request):
	for checkuser in MyUser.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginservice.html')
	form=AddBill(request.POST or None,request.FILES or None)
	next_url=request.GET.get('next')
	data={'form':form,'next':next_url}
	return render(request,'billadd.html',data)
@require_POST
@login_required
def handleBillAdd(request):
	for checkuser in MyUser.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginservice.html')
	form=AddBill(request.POST or None,request.FILES or None)
	next_url=request.GET.get('next')
	data={'form':form,'next':next_url}
	if(form.is_valid()):
		new_bill=form.save(commit=False)
		new_bill.provider=get_object_or_404(ServiceProvider,id=request.user.id)
		new_bill.save()
		form=AddBill()
		return render(request,'billadd.html',{'form':form})
	else:
		return render(request,'billadd.html',data)
@require_GET
@login_required
def renderBillUpdate(request,id):
	for checkuser in MyUser.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginservice.html')
	form=UpdateBill(request.POST or None,request.FILES or None)
	next_url=request.GET.get('next')
	data={'form':form,'next':next_url,'id':id}
	return render(request,'billupdate.html',data)
@require_POST
@login_required
def handleBillUpdate(request,id):
	for checkuser in MyUser.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginservice.html')
	bill=get_object_or_404(Bill,id=id)
	form=UpdateBill(request.POST or None,request.FILES or None,instance=bill)
	next_url=request.GET.get('next')
	data={'form':form,'next':next_url,'id':id}
	if(form.is_valid()):
		bill=form.save(commit=False)
		bill.save()
		form=UpdateBill()
		return render(request,'mainservice.html',{'form':form})
	else:
		return render(request,'BillUpdateForm.html',data)
@require_GET
@login_required
def renderBillDelete(request):
	for checkuser in MyUser.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginservice.html')
	form=DeleteBill(request.POST or None,request.FILES or None)
	next_url=request.GET.get('next')
	data={'form':form,'next':next_url}
	return render(request,'BillDelete.html',data)
@require_POST
@login_required
def handleBillDelete(request):
	for checkuser in MyUser.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginservice.html')
	form=DeleteBill(request.POST)
	next_url=request.GET.get('next')
	data={'form':form,'next':next_url}
	if(form.is_valid()):
		customer_id=form.cleaned_data['customer_id']
		bill=get_object_or_404(Bill,customer_id=customer_id)
		bill.delete()
		bills=Bill.objects.all()
		return render(request,'Bills.html',{'bills':bills})
	else:
		return render(request,'BillDelete.html',data)
@require_GET
@login_required
def renderBillView(request):
	for checkuser in MyUser.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginservice.html')
	form=ViewBill(request.POST or None,request.FILES or None)
	next_url=request.GET.get('next')
	data={'form':form,'next':next_url}
	return render(request,'BillView.html',data)
@require_POST
@login_required
def handleBillView(request):
	for checkuser in MyUser.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginservice.html')
	form=ViewBill(request.POST or None,request.FILES or None)
	next_url=request.GET.get('next')
	#data={'bill':bill,'next':next_url}
	if(form.is_valid()):
		customer_id=form.cleaned_data['customer_id']
		bill=get_object_or_404(Bill,customer_id=customer_id)
		data={'bill':bill,'next':next_url}
		return render(request,'SingleBill.html',data)
	else:
		form=ViewBill(request.POST or None,request.FILES or None)
		data={'form':form,'next':next_url}
		return render(request,'BillView.html',data)
@require_GET
def renderLoginService(request):
	if request.user.is_authenticated():
		for checkuser in MyUser.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginservice.html')
		return redirect('mainservice')
	next_url=request.GET.get('next')
	loginform=LoginFormService()
	data={'loginform':loginform,'next':next_url}
	return render(request,'loginservice.html',data)
@require_GET
def renderSignupService(request):
	if request.user.is_authenticated():
		for checkuser in MyUser.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginservice.html')
		return redirect('mainservice')
	next_url=request.GET.get('next')
	signupform=SignupFormService(initial={'phone':'+91'})
	data={'signupform':signupform,'next':next_url}
	return render(request,'signupservice.html',data)
@require_GET
def mainservice(request):
	if request.user.is_authenticated():
		for checkuser in MyUser.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginservice.html')
		return render(request,'mainservice.html')
	else:
		loginform=LoginFormService()
		return render(request,'loginservice.html',{'loginform':loginform})

@require_GET
@login_required
def logoutservice(request):
	if request.user.is_authenticated():
		logout(request)
		return redirect('mainservice')
@require_POST
def handleLoginService(request):
	
	if request.user.is_authenticated():
		for checkuser in MyUser.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginservice.html')
		return redirect('mainservice')
	f=LoginFormService(request.POST)
	next_url=request.GET.get('next')
	if f.is_valid():
		user=f.get_user()
		login(request,user)
		for checkuser in MyUser.objects.all():
			if checkuser.id==user.id:
				logout(request)
				return render(request,'invalidloginservicelogout.html')
		if not next_url:
			return redirect('mainservice')
		else :
			return redirect(next_url)
	else:
		loginform=f
		signupform=SignupFormService(initial={'phone':'+91'})
		data={'signupform':signupform,'loginform':loginform,'next':next_url}
		return render(request,'loginservice.html',data)
@require_POST
def handleSignupService(request):
	if request.user.is_authenticated():
		for checkuser in MyUser.objects.all():
			if checkuser.id==request.user.id:
				return render(request,'invalidloginservice.html')
		return redirect('mainservice')
	f=SignupFormService(request.POST)
	next_url=request.GET.get('next')
	if f.is_valid():
		user=f.save()
		user.save()
		return redirect('rloginservice')
	else:
		signupform=f
		loginform=LoginFormService()
		data={'signupform':signupform,'loginform':loginform,'next':next_url}
		return render(request,'signupservice.html',data)

	
