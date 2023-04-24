from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Transactions

class RegisterForm(forms.Form):
#form for new student registration'''
    def nothing():
        return ("")


class MobilePaymentForm(forms.Form):
#form for mobile payment '''
    amount = forms.DecimalField(label='Amount', required=True, decimal_places=2, max_value=1000, min_value=1,
                                max_digits=8)
    cellphone = forms.CharField(required=True, max_length=200)
    #details = forms.CharField(label='Details', required=True, max_length=200)

