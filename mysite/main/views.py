# main/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

@login_required(login_url="login")
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login_view(request):
    form = LoginForm()  # Correctly initialize the form
    if request.method == "POST":
        form = LoginForm(data=request.POST)  # Correctly initialize the form with POST data
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  # Use 'login' instead of 'auth.login'
                return redirect("home")

    context = {"form": form}
    return render(request, "login.html", context=context)

def register_view(request):
    form = CreateUserForm()  # Correctly initialize the form
    if request.method == "POST":
        form = CreateUserForm(request.POST)  # Correctly initialize the form with POST data
        if form.is_valid():
            form.save()
            return redirect("login")

    context = {"form": form}
    return render(request, "register.html", context=context)

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the home page or wherever you'd like
