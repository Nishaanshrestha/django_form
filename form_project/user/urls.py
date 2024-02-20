from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signp/', views.signup_view, name='signup'),
    path('home/', views.home, name='home'),
]


