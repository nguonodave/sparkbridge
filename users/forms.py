from django.contrib.auth.forms import UserCreationForm
from .models import User, Customer, Company
from django import forms

class CustomerSignUpForm(UserCreationForm):
    d_o_b = forms.DateField(required=True, widget=forms.DateInput(
        attrs = {
            'type':'date'
        }
    ))

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2', 'd_o_b']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        if commit:
            user.save()
            Customer.objects.create(user=user, d_o_b=self.cleaned_data['d_o_b'])
        return user

class CompanySignUpForm(UserCreationForm):
    field = forms.ChoiceField(choices=Company.choices)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2', 'field']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_company = True
        if commit:
            user.save()
            Company.objects.create(user=user, field=self.cleaned_data['field'])
        return user

