from django.db import models
from django.forms import ModelForm

from .models import Customer, Order
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  # [views.py -->register]

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields ="__all__"

class CustomerForm(ModelForm):  #image profile_info 
    class Meta:
        model = Customer
        fields ="__all__"
        exclude =['user']

class CreateNewUser(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']