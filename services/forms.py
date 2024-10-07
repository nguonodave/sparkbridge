from django import forms
from .models import Service

class CreateNewService(forms.Form):
    name = forms.CharField(max_length=40, required=True)
    description = forms.CharField(widget=forms.Textarea, label='Description', required=True)
    price_hr = forms.DecimalField(decimal_places=2, max_digits=5, min_value=0.00, max_value=999.99, required=True, label="Price per hour")
    field = forms.ChoiceField(required=True)

    def __init__(self, *args, **kwargs):
        # extracting the company parameter to customize field choices
        company = kwargs.pop('company', None)
        super(CreateNewService, self).__init__(*args, **kwargs)

        # adding choices to fields based on the company type
        if company:
            if company.field != 'All in One':
                self.fields['field'].choices = [(company.field, company.field)]
            else:
                self.fields['field'].choices = Service._meta.get_field('field').choices

        # adding placeholders to form fields
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Service Name'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter Description'
        self.fields['price_hr'].widget.attrs['placeholder'] = 'Enter Price per Hour'

        # setting autocomplete to off to turn off previous input suggestions
        self.fields['name'].widget.attrs['autocomplete'] = 'off'

class RequestServiceForm(forms.Form):
    address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Enter your address'}))
    time = forms.IntegerField(min_value=1, max_value=24, widget=forms.NumberInput(attrs={'placeholder': 'Enter time for the service in hours'}))
