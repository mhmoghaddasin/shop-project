from .models import User
from django import forms

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=10, required=True,)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'mobile', 'image', 'password', 'confirm_password']

