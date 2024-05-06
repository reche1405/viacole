from django import forms 
from .models import Service

class RegistrationForm(forms.Form):
    is_buyer = forms.BooleanField(required=False, widget= forms.CheckboxInput(
            
        )
    )
    is_vendor = forms.BooleanField(required=False, widget= forms.CheckboxInput(
           
        ))
    purchase_range = forms.CharField(widget=forms.TextInput(
        attrs = {
            "hidden" : "true"
        }
    ))
    purchase_interests = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs = {
                "hidden" : "true"
            }
        )
    )
    consignment_range = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {
            "hidden" : "true"
        }
    ))
    consignment_interests = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs = {
                "hidden" : "true"
            }
        )
    )