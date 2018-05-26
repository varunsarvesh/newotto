"""ottodc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from bookingapp.views import OrderPage, LoginPage, AdminPanel, Master

BookingApp_url_patterns = [
    path('', LoginPage.as_view()),
    path('admin/', AdminPanel.as_view()),
    path('ExpressForm/', OrderPage.express),
    path('NormalForm/', OrderPage.normal),
    path('importdealers_form/', Master.dealer_import_form),
    path('importdealers/', Master.dealer_import, name="importdealers"),
]
