from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    global trust
    trust = 1
    return render(request, 'labyrinth/home.html')

def keep_walking(request):
    if request.method == 'POST':
            firstbuttonclicked = True
            return render(request, 'labyrinth/keep_walking.html', context = {'firstbuttonclicked' : firstbuttonclicked})
        
    return render(request, 'labyrinth/keep_walking.html', context = {'firstbuttonclicked' : False})

def asleep1(request):
     return render(request, 'labyrinth/asleep1.html', context = {})

def labyrinth_hole(request):
     return render(request, 'labyrinth/labyrinth_hole.html', context = {})

def brace_for_landing(request):
     global trust
     trust = 2
     return render(request, 'labyrinth/brace_for_landing.html', context = {})

def dont_brace_for_landing(request):
     global trust
     trust = 0
     return render(request, 'labyrinth/dont_brace_for_landing.html', context = {})

def follow_parrot(request):
     choice = 'follow'
     action = 'n/a'
     return render(request, 'labyrinth/follow_parrot.html', context = {'trust' : trust, 'choice' : choice, 'action' : action})

def sketchy_parrot(request):
     global trust
     choice = 'sketchy'
     action = 'n/a'
     tree_guess = 'n/a'
     if request.method == 'POST':
          if 'action' in request.POST:
               action = request.POST.get('action')
          elif 'tree_guess' in request.POST:
               action = request.POST.get('action')
               tree_guess = request.POST.get('tree_guess').lower()
               if 'western hemlock' in tree_guess:
                    tree_guess = 'correct'
                    trust = 1
               else:
                    tree_guess = 'incorrect'
                    trust = -1
     return render(request, 'labyrinth/sketchy_parrot.html', context = {'trust' : trust, 'choice' : choice, 'action' : action, 'tree_guess' : tree_guess})

def say_diseased(request):
     global trust 
     trust += 1 # might change later
     return render(request, 'labyrinth/say_diseased.html', context = {})

def say_nothing(request):
     return render(request, 'labyrinth/say_nothing.html', context = {})

def befriend(request):
     return render(request, 'labyrinth/befriend.html', context = {})

# login function for later if I figure out how forms work...
#def signup(request):
#    return render(request, 'labyrinth/signup.html', {})

#def login(request)
#    return render(request, 'labyrinth/login.html', {})


# I'll add in playing as Shaquila later if I have time but I doubt I will ToT
# Shaquila vs The voice in her head
# Based on your first choice, you can either be Shaquilla, or a voice in her head (This will be stored in a variable)
# I want both ways to have the same plotline and meeting the same characters and the same options, but I want the styles to be different
#  Shaquila-choice  style: Light backgrounds, an extra good ending
#  Voice-Choice Style: Darker backgrounds, images of things you couldn't see as Shaquila, an extra bad ending


# Plotline
# Shaquila is a girl who loves nature, has an evil stepmother (uses her for chores) and wants a drought in her town to go away
# While bickering with you, she pricks her finger on a thorn that has anesthetics in it, and it promptly puts her to sleep
# As soon as she falls asleep, you can control her body. Your mind also becomes clearer as she sleeps.
# You remember that your goal was to manipulate her into not stopping the drought.
# You are a fungus that has only recently begun thriving because of the drought.
""" you found your way into Shaquila's brain and you need to find a way to save your populace from dying out.
To help with confusion, Shaquila's voice will be a certain colour, and there will be a real narrator voice from
your true perspective.
"""