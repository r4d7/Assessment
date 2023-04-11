from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'Authentication/home.html')
def login(request):
    return HttpResponse('You are on my login page')