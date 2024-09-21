from typing import Any
from django.contrib.auth.forms import UserCreationForm
from .models import User, Customer, Company
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

class CustomerSignUpForm(UserCreationForm):
    d_o_b = forms.DateField(
        required=True,
        label = "Enter your date of birth",
        widget=forms.DateInput(attrs = {
            'type':'date',
            'class':'date',
        })
    )

    def __init__(self, *args, **kwargs):
        super(CustomerSignUpForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Create your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm the created password'

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2', 'd_o_b']

    def clean_d_o_b(self):
        d_o_b = self.cleaned_data.get('d_o_b')
        current_date = timezone.now().date()
        
        if d_o_b > current_date:
            raise ValidationError("Please enter a valid date of birth.")

        age = current_date.year - d_o_b.year
        if (current_date.month < d_o_b.month) or (current_date.month == d_o_b.month and current_date.day < d_o_b.day):
            age -= 1

        if age < 18:
            raise ValidationError("Sorry, you need to be 18 years and above to use this website.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        if commit:
            user.save()
            Customer.objects.create(user=user, d_o_b=self.cleaned_data['d_o_b'])
        return user

class CompanySignUpForm(UserCreationForm):
    field = forms.ChoiceField(choices=Company.choices)

    def __init__(self, *args, **kwargs):
        super(CompanySignUpForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Create your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm the created password'

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

