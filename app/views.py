from django.contrib.auth import logout as auth_logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import UserRegistration
from django.db import connection
from .forms import EditProfileForm

import razorpay
client = razorpay.Client(auth=("rzp_test_kY71FTFw40NENF", "UAHjDNR6V01i358nRzfJowTK"))

def subscription_view(request):
    return render(request, 'subscription.html')

def website_page(request):
    return render(request, 'website.html')

def our_story_view(request):
    return render(request, 'OurStory.html')

def products_view(request):
    return render(request, 'Products.html')

@login_required
def subscription(request):
    user = request.user
    user_details = {
        'name': user.get_full_name(),
        'email': user.email,
    }
    return render(request, 'subscription.html', {'user_details': user_details})


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            city = form.cleaned_data['city']
            address = form.cleaned_data['address']
            pincode = form.cleaned_data['pincode']
            password = form.cleaned_data['password1']
            phoneNumber = form.cleaned_data['phoneNumber']
            try:
                user = UserRegistration.objects.create_user(username=username, email=email, password=password, city=city, address=address, pincode=pincode, phoneNumber=phoneNumber)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                print("User created successfully:", user.username)
                return redirect('login')
            except Exception as e:
                print("Error occurred while creating user:", e)
                form.add_error(None, "An error occurred while saving the user.")
        else:
            print("Form is invalid:", form.errors)
    else:
        form = RegistrationForm()
    user_data = UserRegistration.objects.all()
    specific_user_data = UserRegistration.objects.values('username', 'email', 'city', 'address', 'pincode', 'password', 'phoneNumber')
    return render(request, 'registration.html', {'form': form, 'user_data': user_data, 'specific_user_data': specific_user_data})


def login(request):
    if request.method == 'POST':
        print("POST data:", request.POST)
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            print("Form is valid")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("User is authenticated")
                auth_login(request, user)
                return redirect('website')
            else:
                print("Invalid username or password")
                messages.info(request, 'Invalid Username or Password')
        else:
            print("Form is not valid")
            print("Form errors:", form.errors)
            messages.error(request, 'Invalid form submission')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    if request.method == 'POST':
        pass
    success_messages = messages.get_messages(request)
    error_messages = messages.get_messages(request)
    
    success_exists = any(message.level == messages.SUCCESS for message in success_messages)
    error_exists = any(message.level == messages.ERROR for message in error_messages)
    
    return render(request, 'dashboard.html', {'success_exists': success_exists, 'error_exists': error_exists})


def transactions(request):
    return render(request, 'transactions.html')


def my_subscriptions(request):
    return render(request, 'my_subscriptions.html')

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User profile updated successfully")
            print("User profile updated successfully:", user.username)
            return redirect('dashboard')
        else:
            print("Form is invalid:", form.errors)
    else:
        user_data = UserRegistration.objects.get(pk=user.pk)

        initial_data = {
            'username': user_data.username,
            'first_name': user_data.first_name,
            'last_name': user_data.last_name,
            'email': user_data.email,
            'city': user_data.city,
            'address': user_data.address,
            'pincode': user_data.pincode,
            'phoneNumber' : user_data.phoneNumber,
        }

        form = EditProfileForm(instance=user, initial=initial_data)

    return render(request, 'edit_profile.html', {'form': form, 'user': user})