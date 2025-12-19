from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('userdashboard/', views.userdashboard, name='userdashboard'),
    path('profile/', views.profile, name='profile'),  
    path('logout/', views.logout, name='logout'),
    
    
    
]
