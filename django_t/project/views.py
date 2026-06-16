# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
  
def task(request):
    return render(request, 'tasks.html')
  
def ticket(request):
    return render(request, 'tickets.html')
  
def products(request):
    return render(request, 'products.html')