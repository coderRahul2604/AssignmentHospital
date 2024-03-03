from django.shortcuts import render, HttpResponse
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from authentication.forms import PatientSignupForm, DoctorSignupForm
from .models import Patient, Doctor
from django.contrib.auth.hashers import check_password
# Create your views here.
def index(request):
    return render(request, 'index.html')

def loginPatient(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            patient = Patient.objects.get(username=username, password=password)
            print(patient)
            # Both username and password match
            messages.success(request, 'Login Successfully')
            return render(request, 'dashboard.html', {'info': [patient]})
        except Patient.DoesNotExist:
            # Username or password is incorrect
            messages.error(request, 'Invalid Credentials')
    
    return render(request, 'index.html')
    


def loginDoctor(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            doctor = Doctor.objects.get(username=username, password=password)
            # Both username and password match
            messages.success(request, 'Login Successfully')
            return render(request, 'dashboard.html', {'info': [doctor]})
        except Doctor.DoesNotExist:
            # Username or password is incorrect
            messages.error(request, 'Invalid Credentials')
    
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        print(user_type)
        if user_type == 'doctor':
            form = DoctorSignupForm(request.POST, request.FILES)
        else:
            form = PatientSignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Signup Successfully')
            return render(request, 'index.html')
    messages.error(request, 'Somthing want wrong.')
    return render(request, 'index.html')

def logout(request):
    auth_logout(request)
    messages.success(request, 'Logout successfully')
    return render(request, 'index.html')
 