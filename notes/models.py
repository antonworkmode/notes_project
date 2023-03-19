# vi notes/models.py

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    # Категория, хранящая заметки.
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='categories'

    def __str__(self):
        # Возврат строкового представления модели.
        return self.text

class Note(models.Model):
    # Заметка, оставленная пользователем в выбранной категории.
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Возврат строкового представления модели.
        return f'{self.text[:50]}...'
