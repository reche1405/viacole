from django import forms 

class RegistrationForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "hidden" : "true"
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "hidden" : "true"
        }
    ))
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "hidden" : "true"
        }
    ))
    budget_range = forms.CharField(widget=forms.TextInput(
        attrs = {
            "hidden" : "true"
        }
    ))


