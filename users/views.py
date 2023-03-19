# vi users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    # Регистрация нового пользователя.
    if request.method != 'POST':
        # Вывод пустой формы для регистрации.
        form = UserCreationForm()
    else:
        # Обработка заполненной формы.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Выполнение входа в учетную запись и перенаправление на домашнюю страницу.
            login(request, new_user)
            return redirect('notes:index')
    # Вывод пустой или недействительной формы.
    context = {'form': form}
    return render(request, 'registration/signup.html', context)
