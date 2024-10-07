from typing import Any
from django.contrib.auth.forms import UserCreationForm
from .models import User, Customer, Company
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

# functionality for customer registration
class CustomerSignUpForm(UserCreationForm):
    # adding (d_o_b) field in customer creation
    d_o_b = forms.DateField(
        required=True,
        label = "Enter your date of birth",
        widget=forms.DateInput(attrs = {
            'type':'date',
            'class':'date',
        })
    )

    # customizing the form fields
    def __init__(self, *args, **kwargs):
        super(CustomerSignUpForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your last name'
        self.fields['password1'].widget.attrs['placeholder'] = 'Create your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm the created password'

    # specifing the model to use (User) and which fields to include in the form
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'd_o_b']

    # validation on the date of birth to ensure it is realistic (not in the future and within an acceptable age range)
    def clean_d_o_b(self):
        d_o_b = self.cleaned_data.get('d_o_b')
        current_date = timezone.now().date()
        
        if d_o_b > current_date:
            raise ValidationError("Ivalid date of birth.")

        age = current_date.year - d_o_b.year

        # ensure effective calculation of age based on month and day (user must reach the month and day for the age to be a complete one year)
        if (current_date.month < d_o_b.month) or (current_date.month == d_o_b.month and current_date.day < d_o_b.day):
            age -= 1

        if age < 18 or age > 100:
            raise ValidationError("Sorry! We only allow 18 years old to 100 years old folks to use this platform.")
        
        return d_o_b

    # set the field is_customer to true and save the user, then create the customer instance
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
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your last name'
        self.fields['password1'].widget.attrs['placeholder'] = 'Create your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm the created password'

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'field']

    # set the field is_company to true and save the user, then create the company instance
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_company = True
        if commit:
            user.save()
            Company.objects.create(user=user, field=self.cleaned_data['field'])
        return user

