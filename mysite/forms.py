from django import forms

class LoginForm(forms.Form):
    iD = forms.CharField(required=False)
    pW = forms.CharField(widget=forms.PasswordInput,required=False)