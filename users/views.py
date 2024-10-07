from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from . models import User
from .forms import CustomerSignUpForm, CompanySignUpForm
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

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

# login functionality
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

# functionality for getting customer's details to display in their profile page
@login_required(login_url='login_user')
def customer_profile(request):
    if not request.user.is_customer:
            error_context = {
                'exclaim': 'Uh-oh!',
                'status': '403 Forbidden',
                'message': "This feature is a customer-only zone. Check out our registration options."
            }
            return HttpResponseForbidden(render(request, "main/errors.html", error_context))

    user = User.objects.get(username=request.user.username)
    
    requested_services = user.customer.requestservice_set.all().order_by('-date')

    # age validation
    d_o_b = user.customer.d_o_b
    current_date = timezone.now().date()
    age = current_date.year - d_o_b.year
    if (current_date.month < d_o_b.month) or (current_date.month == d_o_b.month and current_date.day < d_o_b.day):
        age -= 1

    context = {
        "profile": user,
        "age": age,
        'requested_services': requested_services,
    }

    return render(request, "users/profile.html", context)

# functionality for getting company's details to display in their profile page
def company_profile(request, username):
    user = User.objects.get(username=username)
    services = user.company.service_set.all().order_by('-date')
    context = {
        "profile": user,
        'services': services,
    }
    return render(request, "users/profile.html", context)
