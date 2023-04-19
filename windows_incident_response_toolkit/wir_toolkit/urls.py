from django.urls import path

from . import views

urlpatterns = [
    path('', views.Signin, name='Signin'),
    path('Dashboard', views.Dashboard, name='Dashboard'),
    path('Form', views.Form, name='Form'),
    path('Settings', views.Settings, name='Settings'),
]