from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from . models import User
from .forms import CustomerSignUpForm, CompanySignUpForm

def register(request):
    return render(request, 'users/register.html')

def register_customer(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            return redirect('home')
    else:
        form = CustomerSignUpForm()
    return render(request, 'users/register_customer.html', {'form': form})

def register_company(request):
    if request.method == 'POST':
        form = CompanySignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            return redirect('home')
    else:
        form = CompanySignUpForm()
    return render(request, 'users/register_company.html', {'form': form})

def login_user(request):
    if request.method == "POST":
        # print(request.POST)
        email_input = request.POST['email']
        password_input = request.POST['password']

        try:
            user = User.objects.get(email=email_input)
        except:
            print("email does not exist")

        user = authenticate(request, email=email_input, password=password_input)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("wrong email or password")

    return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')
