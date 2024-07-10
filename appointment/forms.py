# forms.py
from django import forms
from django.utils import timezone


class AppointmentForm(forms.Form):
    speciality = forms.CharField(max_length=100, required=True)
    date = forms.DateField(widget=forms.SelectDateWidget(), required=True)
    start_time = forms.TimeField(widget=forms.TimeInput(format="%H:%M"), required=True)

    def clean_date(self):
        date = self.cleaned_data.get("date")
        if date < timezone.now().date():
            raise forms.ValidationError("The date cannot be in the past!")
        return date
