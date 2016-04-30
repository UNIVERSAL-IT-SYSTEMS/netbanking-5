from django import forms
from .models import *
from .models import ServiceProvider
from django import forms
from account.models import Account
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate
from django.core.validators import MaxValueValidator, MinValueValidator,MinLengthValidator,MaxLengthValidator
class SignupFormService(forms.ModelForm):
	password=forms.CharField(label="password",widget=forms.PasswordInput,validators=[MinLengthValidator(6),MaxLengthValidator(50),])
	password2=forms.CharField(label="confirm password",widget=forms.PasswordInput,validators=[MinLengthValidator(6),MaxLengthValidator(50),])
	company_name=forms.CharField(validators=[MinLengthValidator(6),MaxLengthValidator(50),])
	username=forms.CharField(validators=[MinLengthValidator(6),MaxLengthValidator(50),])
	def clean_password2(self):
		password=self.cleaned_data.get('password')
		password2=self.cleaned_data.get('password2')
		if password and password2 and password!=password2:
			raise forms.ValidationError('password did not matched')
		return password2
	def clean_email(self):
		email_data=self.cleaned_data.get('email')
		if email_data and len(ServiceProvider.objects.filter(email=email_data))>0:
			raise forms.ValidationError('email already exist')
		return email_data
	def clean_accno(self):
		acc_no=self.cleaned_data.get('acc_no')
		if acc_no:
			if len(acc_no)>15 or len(acc_no)<0:
				raise forms.ValidationError('Account number must be a 15 digit number')
			if acc_no:	
				if not len(Account.objects.filter(account_number=acc_no))>0:
					raise forms.ValidationError('bank account number does not exist')
		return acc_no
			
	def __init__(self,*args,**kwargs):
		super(SignupFormService,self).__init__(*args,**kwargs)
		self.fields['email'].required=True
		self.fields['password'].required=True
	def save(self, commit=True):
		user=super(SignupFormService,self).save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user
	class Meta:
		model=ServiceProvider
		fields=['username','email','acc_no','address','company_name']
		help_texts={'acc_no':_("account number length should be of 15 digits"),}
class LoginFormService(forms.Form):
	username=forms.CharField(label='username')
	password=forms.CharField(label='password',widget=forms.PasswordInput)
	def __init__(self,*args,**kwargs):
		self.user_cache=None
		super(LoginFormService,self).__init__(*args,**kwargs)
		#self.fields['username'].required=True
		#self.fields['password'].required=True
	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		if username and password:
			self.user_cache = authenticate(username = username, password = password)
			if self.user_cache is None:
				raise forms.ValidationError('Please enter a correct username and password')
			elif not self.user_cache.is_active:
				raise forms.ValidationError('This account is inactive')
		return self.cleaned_data
	def get_user(self):
		return self.user_cache
class BillPayment(forms.ModelForm):
	class Meta:
		model=Bill
		fields=['customer_id','customer_name','phone_no','date_of_birth']
class AddBill(forms.ModelForm):
	class Meta:
		model=Bill
		fields=['customer_id','customer_name','customer_address','amount']
class UpdateBill(forms.ModelForm):
	class Meta:
		model=Bill
		fields=['customer_id','customer_name','customer_address','amount']
class ViewBill(forms.Form):
	customer_id=forms.CharField(max_length=10)
class DeleteBill(forms.Form):
	customer_id=forms.CharField(max_length=10)
