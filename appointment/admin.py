from django.contrib import admin
from .models import Appointment


# Register your models here.
@admin.register(Appointment)
class AdminAppoint(admin.ModelAdmin):
    list_display = ["patient", "doctor", "specialty", "date", "start_time", "end_time"]
