from django import forms
from .models import Booking


class BookingStatusForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['status']

