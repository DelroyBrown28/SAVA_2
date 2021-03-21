import os
import datetime
from django import forms


# Simple contact form sends email and message
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': "Your Full Name", 'class': 'all-form-inputs'
    }))
    contact = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your contact number", 'class': 'all-form-inputs'
    }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': "Your Email Address", 'class': 'all-form-inputs'
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': "Please leave us a detailed message explaining exactly what you need assistance with", 'class': 'all-form-inputs'
    }))
