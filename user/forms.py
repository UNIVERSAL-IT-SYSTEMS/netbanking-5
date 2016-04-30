from .models import MyUser
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate
from django.core.validators import MaxValueValidator, MinValueValidator,MinLengthValidator,MaxLengthValidator
from account.models import Account
class SignupForm(forms.ModelForm):
	password=forms.CharField(label="password",widget=forms.PasswordInput,validators=[MinLengthValidator(6),MaxLengthValidator(50),])
	password2=forms.CharField(label="confirm password",widget=forms.PasswordInput,validators=[MinLengthValidator(6),MaxLengthValidator(50),])
	first_name=forms.CharField(validators=[MinLengthValidator(6),MaxLengthValidator(50),])
	last_name=forms.CharField(validators=[MinLengthValidator(6),MaxLengthValidator(50),])
	username=forms.CharField(validators=[MinLengthValidator(6),MaxLengthValidator(50),])
	address=forms.CharField(validators=[MinLengthValidator(6),MaxLengthValidator(50),])
	def clean_password2(self):
		password=self.cleaned_data.get('password')
		password2=self.cleaned_data.get('password2')
		if password and password2 and password!=password2:
			raise forms.ValidationError('password did not match')
		return password2
	def clean_email(self):
		email_data=self.cleaned_data.get('email')
		if email_data and len(MyUser.objects.filter(email=email_data))>0:
			raise forms.ValidationError('email already exists')
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
		super(SignupForm,self).__init__(*args,**kwargs)
		self.fields['email'].required=True
		self.fields['password'].required=True
	
	def save(self, commit=True):
		user=super(SignupForm,self).save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user 
	def clean_father(self):
		clean_father=super(SignupForm,self).clean()
		
		father_name=clean_father.get('father_name')
		if father_name:
			if len(father_name)<6:
				raise forms.ValidationError('Father name length must be between 6 to 50 characters')
		return father_name
	def clean_usename(self):
		username=self.cleaned_data['username']
		if username:
			if len(username)<6 or len(username)>15:
				raise forms.ValidationError('username length must be between 6 to 15 characters')
		return username 
			
	class Meta:
		model=MyUser
		fields=['first_name','last_name','father_name','acc_no','phone','dob','address','username','email','signature']
		help_texts={'dob':_("dd-mm-yyyy"),'acc_no':_("account number length should be of 15 digits"),'phone':_("phone number length should be of 10 digits")}
		error_messages={'acc_no':{'MaxValueValidator':_("length should be of 15 digits"),},}
  
class LoginForm(forms.Form):
	username=forms.CharField(label='username')
	password=forms.CharField(label='password',widget=forms.PasswordInput)

	def __init__(self,*args,**kwargs):
		self.user_cache=None
		super(LoginForm,self).__init__(*args,**kwargs)

	def clean(self):
		username=self.cleaned_data.get('username')
		password=self.cleaned_data.get('password')
		if username and password:
			self.user_cache=authenticate(username=username , password=password)
			if self.user_cache is None:
				raise forms.ValidationError('Please Enter a Correct username and password')
			elif not self.user_cache.is_active:
				raise forms.ValidationError('This Account is Inactive')
		return self.cleaned_data 
	def get_user(self):
		return self.user_cache
