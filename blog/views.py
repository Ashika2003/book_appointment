from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog
from base.models import Profile


@login_required
def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect("blog_detail", pk=blog.pk)
    else:
        form = BlogForm()
    return render(request, "blog/create_blog.html", {"form": form})


@login_required
def read_blogs(request):
    mental_health = Blog.objects.filter(category="Mental Health")
    heart_disease = Blog.objects.filter(category="Heart Disease")
    covid_19 = Blog.objects.filter(category="Covid19")
    immunization = Blog.objects.filter(category="Immunization")
    return render(
        request,
        "blog/read_blog.html",
        {
            "mental_health": mental_health,
            "heart_disease": heart_disease,
            "covid19": covid_19,
            "immunization": immunization,
        },
    )


# for doctor to view his posts
@login_required
def read_blogs_by_user(request):
    user = request.user
    blogs = Blog.objects.filter(user=user)
    return render(request, "blog/read_blog_by_user.html", {"blogs": blogs})
