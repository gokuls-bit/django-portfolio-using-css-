# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # URL for the main portfolio page
    path('', views.home, name='home'),
    # URL to handle the contact form submission
    path('contact/', views.contact_submit, name='contact_submit'),
]