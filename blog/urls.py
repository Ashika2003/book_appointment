from django.urls import path
from blog import views


urlpatterns = [
    path("create/", views.create_blog, name="create-blog"),
    path("view/", views.read_blogs, name="read-blogs"),
    path("view/user", views.read_blogs_by_user, name="read-blogs-by_user"),
]
