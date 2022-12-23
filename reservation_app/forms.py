from django import forms
from .models import Reservation
from datetime import date


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


PERSON_NUMBER = [
    ('Seelect Person', 'Select Person'),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
]


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
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
            'date': DateInput(attrs={
                'class': 'form-control',
                'id': 'input_date',
                'name': 'date',
            }),
            'time': TimeInput(attrs={
                'class': 'time form-control picker__input',
                'id': 'input_time',
            }),
            'number': forms.Select(attrs={
                'class': 'form-control',
                'id': 'person',
                'placeholder': 'Select Person'
            }, choices=PERSON_NUMBER)
        }

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

    def clean_date(self):
        chosen_date = self.cleaned_data.get('date')
        current_date = date.today()

        if chosen_date.year > current_date.year or chosen_date.year < current_date.year:
            raise forms.ValidationError('Please select the correct date')

        elif chosen_date.month < current_date.month or chosen_date.day < current_date.day:
            raise forms.ValidationError('Please select the correct date')

        return chosen_date

