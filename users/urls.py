from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("profile/<str:username>/", views.user_profile, name="user_profile"),
]
