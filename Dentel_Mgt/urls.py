from django.conf.urls import include
from django.contrib import admin
from django.urls import path

import Home
from Home import urls
import StaffApp
from StaffApp import urls
import Patient
from Patient import urls
from Doctor import urls
import Doctor
import Bookings
from Bookings import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(Home.urls)),
    path("StaffApp/",include(StaffApp.urls)),
    path("Patient/",include(Patient.urls)),
    path("Doctor/",include(Doctor.urls)),
    path("Bookings/",include(Bookings.urls)),
    
]
