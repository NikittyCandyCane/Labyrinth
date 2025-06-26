from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'labrynth/home.html')

def keep_walking(request):
    return render(request, 'labrynth/keep_walking.html')

# login function for later if I figure out how forms work...
def signup(request):
    return render(request, 'labrynth/signup.html', {})

def login(request)
    return render(request, 'labrynth/login.html', {})