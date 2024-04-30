from django import forms 
from allauth.account.forms import SignupForm
from .models import Service

class RegistrationForm(SignupForm):
    is_buyer = forms.BooleanField()
    is_vendor = forms.BooleanField()
    purchase_range = forms.CharField(widget=forms.TextInput(
        attrs = {
            "hidden" : "true"
        }
    ))
    purchase_interests = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    consignment_range = forms.CharField(widget=forms.TextInput(
        attrs = {
            "hidden" : "true"
        }
    ))
    consignment_interests = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
