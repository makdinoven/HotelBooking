from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'patronymic', 'phone_number', 'email', 'check_in_date', 'check_out_date']
