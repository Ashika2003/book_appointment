from django.urls import path
from base import views


urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.signup, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.custom_logout, name="logout"),
    path("patient_dashboard/", views.patient_dashboard, name="patient_dashboard"),
    path("doctor_dashboard/", views.doctor_dashboard, name="doctor_dashboard"),
]
