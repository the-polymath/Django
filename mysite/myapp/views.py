from django.shortcuts import render
from django.http import HttpResponse
from .models import Items, ToDoList
# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, 'myapp/view.html', {"ls": ls})

def home(response):
    return render(response, 'myapp/home.html', {})
