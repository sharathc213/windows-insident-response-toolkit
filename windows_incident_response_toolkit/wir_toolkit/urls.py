from django.urls import path

from . import views

urlpatterns = [
    path('', views.Signin, name='Signin'),
    path('Dashboard/<str:param>/', views.Dashboard, name='Dashboard'),
    path('Dashboard', views.Dashboard, name='Dashboard'),
    path('AddComputer', views.AddComputer, name='Computer'),
    path('Scan/<str:param>/', views.Scan, name='Scan'),
    path('Delete/<str:param>/', views.Delete, name='Delete'),
    path('addcom', views.addcom, name='addcom'),
    path('action', views.action, name='action'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]