from django.shortcuts import render, redirect
from .forms import CustomerSignUpForm

def register_customer(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            return redirect('home')
    else:
        form = CustomerSignUpForm()
    return render(request, 'users/register_customer.html', {'form': form})
