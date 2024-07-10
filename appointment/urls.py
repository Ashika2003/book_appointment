from django.urls import path
from . import views


urlpatterns = [
    path("list/", views.list_doctor, name="list-doctors"),
    path(
        "book_appointment/<int:doctor_id>/",
        views.book_appointment,
        name="book-appointment",
    ),
    path(
        "appointment/<int:appointment_id>/",
        views.appointment_details,
        name="appointment_details",
    ),
]
