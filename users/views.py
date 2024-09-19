from django.shortcuts import render, redirect
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
    return render(request, 'users/login.html')
