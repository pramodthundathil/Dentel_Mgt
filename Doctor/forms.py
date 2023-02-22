from django.forms import ModelForm
from .models import DoctorList


class DoctorListAddForm(ModelForm):
    class Meta:
        model = DoctorList
        fields = ["DoctorName","Doctor_spec","Doctor_Edu"]