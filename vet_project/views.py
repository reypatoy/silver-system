from django.contrib import auth
from pathlib import Path

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_view(request):
    error_message = None
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            print("user ----------------------------", user)

            if user is not None:

                login(request, user)

                if request.GET.get("next"):
                    return redirect(request.GET.get("next"))

                else:
                    if user.user_type == 1:
                        return redirect("crm:admin_dashboard_view")

                    if user.user_type == 2:
                        pass

                    if user.user_type == 3:
                        pass

        else:
            error_message = form.errors

    context = {"form": form, "error_message": error_message}

    # sample = {"test": "hello", "test2": 5555}

    return render(request, "auth/login.html", context)
