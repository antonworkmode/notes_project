# vi notes/admin.py

from django.contrib import admin
from .models import Category, Note

admin.site.register(Category)
admin.site.register(Note)
