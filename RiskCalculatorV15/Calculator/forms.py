from django import forms
from .models import AssetsModel
from django.core.exceptions import ValidationError


# create a ModelForm
class AssetsForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = AssetsModel
        fields = [
            'interest_rate',
            'dividend_stock',
            'growth_stock',
            'state_bond',
            'corporate_floater',
            'gold' 
        ]
        




