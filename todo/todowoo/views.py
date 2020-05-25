from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from .forms import TodoForm
from .models import Todo


def home(request):
    return render(request, 'todowoo/home.html')


def signup_user(request):
    if request.method == 'GET':
        return render(request, 'todowoo/signup_user.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('current_todos')

            except IntegrityError:
                return render(request, 'todowoo/signup_user.html', {'form': UserCreationForm(), 'error': 'That username has already been taken. Choose another one.'})
        else:
            return render(request, 'todowoo/signup_user.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})


def login_user(request):
    if request.method == 'GET':
        return render(request, 'todowoo/login_user.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todowoo/login_user.html', {'form': AuthenticationForm(), 'error': 'User and password did not match'})
        else:
            login(request, user)
            return redirect('current_todos')


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def create_todos(request):
    if request.method == 'GET':
        return render(request, 'todowoo/create_todo.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect('current_todos')
        except ValueError:
            return render(request, 'todowoo/create_todo.html', {'form': TodoForm(), 'error': 'Bad data passed in. Try again'})


def current_todos(request):
    todos = Todo.objects.filter(user=request.user, completed__isnull=True)
    return render(request, 'todowoo/current_todos.html', {'todos': todos})

