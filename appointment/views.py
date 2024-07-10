from base.models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Appointment
import datetime
from .forms import AppointmentForm
from base.models import Profile
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Define the scopes
SCOPES = ["https://www.googleapis.com/auth/calendar"]


from google_auth_oauthlib.flow import InstalledAppFlow

# Define the scopes
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def create_calendar_event(doctor, patient, date, start_time, end_time, specialty):
    # Create OAuth2 credentials flow
    flow = InstalledAppFlow.from_client_secrets_file(
        "appointment/secret_key.json", SCOPES, redirect_uri="http://localhost:8080/"
    )
    flow.redirect_uri = "http://localhost:8080/"
    credentials = flow.run_local_server(port=8080)

    # Build the service
    service = build("calendar", "v3", credentials=credentials)

    # Define the event
    event = {
        "summary": f"Appointment with {patient.username}",
        "location": "Location details here",
        "description": f"Specialty: {specialty}",
        "start": {
            "dateTime": datetime.datetime.combine(date, start_time).isoformat(),
            "timeZone": "UTC",
        },
        "end": {
            "dateTime": datetime.datetime.combine(date, end_time).isoformat(),
            "timeZone": "UTC",
        },
        "attendees": [
            {"email": doctor.user.email},
            {"email": patient.email},
        ],
    }

    # Insert the event into the calendar
    event = service.events().insert(calendarId="primary", body=event).execute()
    url = event.get("htmlLink")
    return url


# Create your views here.
@login_required
def list_doctor(request):
    doctors = Profile.objects.filter(role="DOCTOR")
    return render(request, "appointment/doctor_list.html", {"doctors": doctors})


@login_required
def appointment_details(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    return render(
        request, "appointment/appointment_details.html", {"appointment": appointment}
    )


@login_required
def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Profile, id=doctor_id, role="DOCTOR")
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            specialty = form.cleaned_data["speciality"]
            date = form.cleaned_data["date"]
            start_time = form.cleaned_data["start_time"]
            end_time = (
                datetime.datetime.combine(date, start_time)
                + datetime.timedelta(minutes=45)
            ).time()

            # Create a calendar event
            url = create_calendar_event(
                doctor, request.user, date, start_time, end_time, specialty
            )

            # Create the appointment
            appointment = Appointment.objects.create(
                doctor=doctor.user,
                patient=request.user,
                specialty=specialty,
                date=date,
                start_time=start_time,
                end_time=end_time,
                url=url,
            )

            # Redirect to a success page or the doctor's calendar
            return redirect("appointment_details", appointment_id=appointment.id)
    else:
        form = AppointmentForm()
    return render(
        request, "appointment/appointment.html", {"form": form, "doctor": doctor}
    )
