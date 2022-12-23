from django import forms
from .models import ContactUs

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        exclude = ('created_at',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'Your Name',
                'name': 'name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'Your Email',
                'name': 'email',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'phone',
                'placeholder': 'Your Number',
                'name': 'phone',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'message',
                'placeholder': 'Your Message',
            })}

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if len(phone) < 11:
            raise forms.ValidationError('The phone number must be at least 11 numbers')

        elif phone[0:3] == '+98':
            raise forms.ValidationError('Please enter valid phone number !!')

        elif phone:
            try:
                int(phone)
            except:
                raise forms.ValidationError('Please enter valid phone number !!')

        return phone

