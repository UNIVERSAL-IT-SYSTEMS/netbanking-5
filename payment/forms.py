from django import forms
from maintainbill.models import *
from user.models import *




class EnterCustomerId(forms.Form):
	serviceprovider=forms.ModelChoiceField(queryset=ServiceProvider.objects.all().order_by('company_name'))
	customer_id=forms.CharField(max_length=10)
class EnterOtp(forms.Form):
	OneTimePassword=forms.IntegerField()
	def clean(self):
		cleaned_data=super(EnterOtp,self).clean()
		otp=cleaned_data.get('OneTimePassword')
		if otp!=123456:
			raise forms.ValidationError("Invalid OTP")
		return otp

