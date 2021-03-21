from django import forms


# Simple contact form sends email and message to store owner
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': "Your Full Name. . ."
    }))
    
    
    contact = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Your contact number. . ."
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': "Your Email Address. . ."
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': "Please leave a message with your name and contact number..."
    }))
