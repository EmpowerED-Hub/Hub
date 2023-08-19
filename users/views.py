from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import UserProfileForm
from .models import UserProfile


def register_user(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect("home")
    else:
        user_form = UserCreationForm()
        profile_form = UserProfileForm()
    return render(
        request,
        "users/register.html",
        {"user_form": user_form, "profile_form": profile_form},
    )


def user_profile(request, username):
    user = User.objects.get(username=username)
    profile = UserProfile.objects.get(user=user)
    context = {"user": user, "profile": profile}
    return render(request, "users/profile.html", context)
