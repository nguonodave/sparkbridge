from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from . models import User
from .forms import CustomerSignUpForm, CompanySignUpForm
from django.contrib import messages

def register(request):
    return render(request, 'users/register.html')

def register_customer(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            login(request, user)
            return redirect('home')
    else:
        form = CustomerSignUpForm()
    return render(request, 'users/register_customer.html', {'form': form})

def register_company(request):
    if request.method == 'POST':
        form = CompanySignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            login(request, user)
            return redirect('home')
    else:
        form = CompanySignUpForm()
    return render(request, 'users/register_company.html', {'form': form})

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        # print(request.POST)
        email_input = request.POST['email']
        password_input = request.POST['password']

        try:
            user = User.objects.get(email=email_input)
        except:
            messages.error(request, "We could not find and account with that email.")
            return render(request, 'users/login.html')

        user = authenticate(request, email=email_input, password=password_input)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Incorrect password. Try again.")

    return render(request, 'users/login.html')

def profile(request, username):
    user = User.objects.get(username=username)
    context = {
        "profile": user,
    }
    if user.is_company:
        services = user.company.service_set.all().order_by('-date')
        context['services'] = services

    return render(request, "users/profile.html", context)
