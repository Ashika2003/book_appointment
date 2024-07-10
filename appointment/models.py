from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey(
        User, related_name="patient_appointments", on_delete=models.CASCADE
    )
    doctor = models.ForeignKey(
        User, related_name="doctor_appointments", on_delete=models.CASCADE
    )
    specialty = models.CharField(max_length=50)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    url = models.URLField()

    def __str__(self):
        return f"{self.patient.username} with Dr. {self.doctor.username} on {self.date} at {self.start_time}"
