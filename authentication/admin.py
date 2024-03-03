from django.contrib import admin
from authentication.models import Patient, Doctor

# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display=['username','email','city']

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display=['username','email','city']