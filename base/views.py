from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from .models import Profile
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def home(request):
    return render(request, "base/home.html")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "base/registers.html", {"form": form})


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)

                # Get the user's profile
                try:
                    profile = Profile.objects.get(user=user)
                except Profile.DoesNotExist:
                    # Handle the case where profile doesn't exist
                    return render(
                        request, "base/login.html", {"error": "Profile does not exist."}
                    )

                # Check if the user is a doctor and redirect accordingly

                if profile.role == "DOCTOR":
                    return redirect("doctor_dashboard")
                else:
                    return redirect("patient_dashboard")
            else:
                # Handle inactive user case
                return render(
                    request, "base/login.html", {"error": "Your account is inactive."}
                )
        else:
            # Handle invalid login case
            return render(
                request, "base/login.html", {"error": "Invalid username or password."}
            )

    return render(request, "base/login.html")


def custom_logout(request):
    logout(request)
    return redirect("home")


@login_required
def patient_dashboard(request):
    profile = Profile.objects.get(user=request.user)
    # Add any additional context data you want to pass to the template
    return render(request, "base/patient_dashboard.html", {"profile": profile})


@login_required
def doctor_dashboard(request):
    profile = Profile.objects.get(user=request.user)
    # Add any additional context data you want to pass to the template
    return render(request, "base/doctor_dashboard.html", {"profile": profile})
