from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'
        widgets={
            'booking_date':DateInput()
        }
        labels={
            'p_name':"Patient Name:",
            'p_phone':"phone:",
            'p_email':"email:",
            'doc_name':"doctor",
            'bookimg_date':"Booking Date:", 


        }