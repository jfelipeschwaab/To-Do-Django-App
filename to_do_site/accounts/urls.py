from django.contrib import admin
from django.urls import path, include
from .views import registro, login_view, logout_view



urlpatterns = [
    path('', registro, name='registro' ),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout')
]