from django import forms
from .models import Company, Client


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'description']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['company', 'name', 'email', 'phone', 'responsible']
