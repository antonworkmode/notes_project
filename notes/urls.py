# vi notes/urls.py

# Определение схемы URL для приложения notes.
from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.category, name='category'),
    path('new_category/', views.new_category, name='new_category'),
    path('new_note/<int:category_id>/', views.new_note, name='new_note'),
    path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),
]
