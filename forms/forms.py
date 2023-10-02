from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['fullname', 'email', 'services', 'subject']
        
        widgets = {
            'fullname': forms.TextInput(attrs={'placeholder': 'Your name..', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email address..', 'required': True}),
            'services': forms.TextInput(attrs={'placeholder': 'E.g Web Development..', 'required': True}),
            'subject': forms.Textarea(attrs={'placeholder': 'Describe your request here...', 'style': 'height:200px', 'required': True}),
        }
