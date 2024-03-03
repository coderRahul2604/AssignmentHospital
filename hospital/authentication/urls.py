from django.urls import path
from authentication import views

urlpatterns = [
    path('', views.index, name='home'),
    path('loginPatient', views.loginPatient, name='Patient'),
    path('loginDoctor', views.loginDoctor, name='Doctor'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='signup'),
]