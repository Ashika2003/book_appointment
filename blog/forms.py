from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "image", "category", "summary", "content", "draft"]

        # Customizing the widgets if necessary
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "summary": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "draft": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

        # Optionally, you can add labels
        labels = {
            "title": "Blog Title",
            "image": "Blog Image",
            "category": "Category",
            "summary": "Summary",
            "content": "Content",
            "draft": "Draft",
        }
