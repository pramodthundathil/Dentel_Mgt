from django.urls import path
from .import views

urlpatterns = [
    path("StaffIndex",views.StaffIndex,name="StaffIndex"),
    path("BookingView/<str:pk>",views.BookingView,name="BookingView"),
    path("AddStaff",views.AddStaff,name="AddStaff"),
    path("AddPatientProfile/<str:pk>",views.AddPatientProfile,name="AddPatientProfile"),
    path("UpdateProfile/<str:pk>,<str:sk>",views.UpdateProfile,name="UpdateProfile"),
    path("PatientList",views.PatientList,name="PatientList"),
    path("DeleteProfile,<str:pk>",views.DeleteProfile,name="DeleteProfile"),
    path("DoctorView",views.DoctorView,name="DoctorView"),
    path("BillView",views.BillView,name="BillView"),
    path("AddBill/<str:pk>",views.AddBill,name="AddBill")
    
]
