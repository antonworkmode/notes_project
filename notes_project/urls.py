# vi notes_project/urls.py

# Определение схемы URL для проекта notes_project.
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),
    path('users/', include('users.urls')),
]
