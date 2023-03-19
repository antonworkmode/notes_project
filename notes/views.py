# vi notes/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Category, Note
from .forms import CategoryForm, NoteForm

def index(request):
    # Домашняя страница приложения notes.
    return render(request, 'notes/index.html')

@login_required
def categories(request):
    # Вывод списка категорий.
    categories = Category.objects.filter(owner=request.user).order_by('date_added')
    context = {'categories': categories}
    return render(request, 'notes/categories.html', context)

@login_required
def category(request, category_id):
    # Вывод выбранной категории и всех хранящихся в ней заметок.
    category = get_object_or_404(Category, id=category_id)
    # Проверка того, что данная категория принадлежит текущему пользователю.
    if category.owner != request.user:
        raise Http404
    notes = category.note_set.order_by('-date_added')
    context = {'category': category, 'notes': notes}
    return render(request, 'notes/category.html', context)

@login_required
def new_category(request):
    # Добавление новой категории.
    if request.method != 'POST':
        # Данные не отправлены; создание пустой формы.
        form = CategoryForm()
    else:
        # Отправка данных POST; обработка данных.
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.owner = request.user
            new_category.save()
            return redirect('notes:categories')
    # Вывод пустой или недействительной формы.
    context={'form': form}
    return render(request, 'notes/new_category.html', context)

@login_required
def new_note(request, category_id):
    # Добавление новой заметки в выбранную категорию.
    category = Category.objects.get(id=category_id)
    if request.method != 'POST':
        # Данные не отправлены; создание пустой формы.
        form = NoteForm()
    else:
        # Отправка данных POST; обработка данных.
        form = NoteForm(data=request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.category = category
            new_note.save()
            return redirect('notes:category', category_id=category_id)
    # Вывод пустой или недействительной формы.
    context={'category': category, 'form': form}
    return render(request, 'notes/new_note.html', context)

@login_required
def edit_note(request, note_id):
    # Редактирование существующей заметки.
    note = Note.objects.get(id=note_id)
    category = note.category
    if category.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # Исходный запрос; заполнение формы данными из текущей заметки.
        form = NoteForm(instance=note)
    else:
        # Отправка данных POST; обработка данных.
        form = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:category', category_id=category.id)
    context = {'note': note, 'category': category, 'form': form}
    return render(request, 'notes/edit_note.html', context)
