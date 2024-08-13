from django.contrib import admin
from django.urls import path, include
from .views import *




urlpatterns = [
    path('notes/', notes, name='notes'),
    path('notes/create/', create_note, name='create_note'),
    path('notes/delete/<int:note_id>/', delete_note_view, name='delete_note'),
    path('notes/edit/<int:note_id>/', edit_note_view, name='edit_note'),

]