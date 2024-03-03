from django import forms
from .models import Patient, Doctor

class PatientSignupForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorSignupForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
