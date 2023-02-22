from django.urls import path
from .import views

urlpatterns = [
    path("DoctorIndex",views.DoctorIndex,name="DoctorIndex"),
    path("AddDoctor",views.AddDoctor,name="AddDoctor"),
    path("AddSummery/<str:pk>",views.AddSummery,name="AddSummery")
    
]
