from django.shortcuts import render,redirect
from django.contrib import messages
from Bookings.models import Booking
from Patient.models import PatientProfile,TreatmetHistory

# Create your views here.

def MyAppointments(request):
    book = Booking.objects.filter(user = request.user)
    context = {
        "book":book
    }
    return render(request,'myappointments.html',context)

def CancelBooking(request,pk):
    Booking.objects.get(id = pk).delete()
    messages.info(request,"Booking Cancelled")
    return redirect('Index')

def TreatmentHistory(request):
    patientpro = PatientProfile.objects.get(PatientId = request.user)
    treat = TreatmetHistory.objects.filter(Patient = patientpro)
    context = {
        "treat":treat
    }
    return render(request,"treatmenthistory.html",context)