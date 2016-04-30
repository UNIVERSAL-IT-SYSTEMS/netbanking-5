from .models import *
from django import forms
class TransferForm(forms.ModelForm):
	class Meta:
		model=Transaction
		fields=['Transfer_to','Amount_used']
	
