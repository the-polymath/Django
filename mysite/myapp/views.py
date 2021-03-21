from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("<h1>This is the first webpage</h1>")

def home(response):
    return HttpResponse("<h1>This is the Second page</h1>")
