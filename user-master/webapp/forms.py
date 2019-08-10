from django import forms
from django.contrib.auth.models import User

class signupForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']
        help_texts = {
            'username': None,
            'email': None,
        }


class SentForm(forms.Form):
	name = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))
	subject = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}))
	message = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 8, 'cols': 70}))

