from django.urls import path

from . import views

urlpatterns = [
    path('', views.Signin, name='Signin'),
    path('Dashboard', views.Dashboard, name='Dashboard'),
    path('AddComputer', views.AddComputer, name='Computer'),
    # path('Settings', views.Settings, name='Settings'),
]