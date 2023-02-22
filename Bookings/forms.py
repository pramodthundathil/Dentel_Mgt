from django.forms import ModelForm,TextInput
from .models import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ["Date","Time","Doctor"]
        
        widgets  = {
            "Date":TextInput(attrs={"type":"date","id":"date1"}),
            "Time":TextInput(attrs={"type":"time"}),
        }