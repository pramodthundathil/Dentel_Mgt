from django.shortcuts import render,redirect
from Home.forms import UserAddForm
from django.contrib.auth.models import User, Group
from django.contrib import messages
from Bookings.models import Booking
from Patient.models import PatientProfile,TreatmetHistory
from Doctor.models import DoctorList
from django.http import HttpResponse

# Create your views here.
def AddStaff(request):
    form = UserAddForm()
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username  = form.cleaned_data.get('username')

            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Already exists")
                return redirect('AddStaff')
            
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email Already taken")
                return redirect('AddStaff')
            
            else:
                new_user = form.save()
                group = Group.objects.get(name='staff')
                new_user.groups.add(group) 
                new_user.save()
                
                messages.success(request,"Staff Created Successfully...")
                return redirect('AddStaff')
    context = {
        'form':form,
    
    }
    return render(request,"staff/addstaff.html",context)

def StaffIndex(request):
    bookings = Booking.objects.all()
    context = {
        "bookings":bookings
    }
    return render(request,"staff/staffhome.html",context)


def BookingView(request,pk):
    group = request.user.groups.all()[0].name
    booking = Booking.objects.filter(id = pk)
    bookingget = Booking.objects.get(id= pk)
    Patient = PatientProfile.objects.filter(PatientId = bookingget.user )
    Patient1 = PatientProfile.objects.get(PatientId = bookingget.user )
    treatment = TreatmetHistory.objects.filter(Patient = Patient1)
    context = {
        "group":group,
        "booking":booking,
        "Patient":Patient,
        "lenpa":Patient.count(),
        "pk":pk,
        "treatment":treatment
        
    }
    if group == "staff":
        return render(request,"staff/patientprofile.html",context)
    elif group == "doctor":
        return render(request,"doctor/patientprofile.html",context)
    else:
        return HttpResponse("<h2 style='color:orange;text-align:center'>You are not autherise to view This Page</h2>")

def AddPatientProfile(request,pk):
    if request.method == "POST":
        pname = request.POST['pname']
        place = request.POST['place']
        phone = request.POST['pnum']
        treat = request.POST["trment"]
        bookingget = Booking.objects.get(id= pk)
        
        profile = PatientProfile.objects.create(PatientName = pname,Place = place,PhoneNumber = phone,Treatment = treat,PatientId = bookingget.user,Doctor = bookingget.Doctor)
        profile.save()
        messages.info(request,"Profile Updated")
    return redirect('BookingView',pk=pk)

def UpdateProfile(request,pk,sk):
    if request.method == "POST":
        profile = PatientProfile.objects.get(id=pk)
        
        profile.PatientName = request.POST["pname"]
        profile.Place = request.POST["place"]
        profile.PhoneNumber = request.POST["pnum"]
        profile.Treatment = request.POST["trment"]
        profile.save()
        messages.info(request,"Profile Updated")
    return redirect('BookingView',pk = sk)

def PatientList(request):
    group = request.user.groups.all()[0].name
    profile = PatientProfile.objects.all()
    context = {
        "profile":profile
    }
    if group == "staff":
        return render(request,"staff/patientview.html",context)
    elif group == "doctor":
        return render(request,"doctor/patientview.html",context)
    else:
        return HttpResponse("<h2 style='color:orange;text-align:center'>You are not autherise to view This Page</h2>")
        

def DeleteProfile(request,pk):
    PatientProfile.objects.get(id = pk).delete()
    messages.info(request,"Profile Deleted")
    return redirect('PatientList')

def DoctorView(request):
    doctor = DoctorList.objects.all()
    context = {
        "doctor":doctor
    }
    return render(request,"staff/doctorview.html",context)
