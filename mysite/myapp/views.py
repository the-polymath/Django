from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Items, ToDoList
from .forms import NewList
# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, 'myapp/view.html', {"ls": ls})

def home(response):
    return render(response, 'myapp/home.html', {})

def create(response):
    if response.method == "POST":
        form = NewList(response.POST)

        if form.is_valid():
            d = form.cleaned_data["name"]
            response.user.todolist_set.create(name=d)
            
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = NewList()
    return render(response, 'myapp/create.html', {"form": form})
