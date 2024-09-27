from django.shortcuts import render, redirect
from rescueready.models import Patient, Driver, Paramedic
from django.contrib.auth import login, authenticate
def home(request):
    return render(request, 'registration.htm')

def home(request):
    return render(request, 'master.htm')

from django.contrib.auth.models import User  # Import the correct model

def paramedic(request):
    username = request.POST.get('username')  # Get username from POST data
    try:
        username_details = User.objects.get(username=username)  # Query using the User model
    except User.DoesNotExist:
        return render(request, 'error.html', {'message': 'User not found'})

    # Continue processing with username_details
    return render(request, 'success.html', {'username': username_details})


def checkview(request):
    username = request.POST['paramedic-username']
    password = request.POST['paramedic-password']

    if Paramedic.objects.filter(name=Paramedic).exists():
        return redirect('/'+Paramedic+'/?password='+password)
    else:
        new_user = username.objects.create(name=room)
        new_user.save();
        return redirect('/'+Paramedic+'/?password='+password)
    

from django.http import HttpResponse
from .models import User  # Assuming you have a User model

def register_user(request):
    if request.user.is_authenticated:  # If the user is logged in or already registered
        return redirect('already_registered')
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('success_page')) 
        # Get the form data
        username = request.POST.get('username')
        hospital_id = request.POST.get('hospital_id')

        # Check if the user with this username or hospital ID already exists
        if User.objects.filter(username=username).exists() or User.objects.filter(hospital_id=hospital_id).exists():
            # Redirect to a page informing the user that they are already registered
            return redirect('already_registered')  # Replace with the name of the URL where they will be redirected

        # If the user is not registered, proceed with the registration process
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        hospital = request.POST.get('hospital')
        password = request.POST.get('password')

        # Save the new user (this assumes you have a User model)
        new_user = User.objects.create(
            name=name,
            age=age,
            gender=gender,
            hospital=hospital,
            hospital_id=hospital_id,
            username=username,
            password=password  # Make sure you hash the password!
        )
        new_user.save()

        # Redirect to success page after registration
        return redirect('success_page')

    return render(request, 'registration.htm')  # Show the registration form if GET request

def already_registered(request):
    return render(request, 'already_registered.html')  # Render a page indicating they are already registered

def success_page(request):
    return render(request, 'success.html', {'message': 'Registration successful as driver!'})



