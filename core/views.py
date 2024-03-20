from django.contrib.auth import login
from django.shortcuts import render, redirect
from django. contrib. auth.models import User, auth
from django .contrib import messages

from .forms import SignUpForm

# Create your views here.
def frontpage (request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:  # if user is valid
            auth.login(request, user)
            return redirect('/')
        else:  # user not valid
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
        
    else:
        return render(request, 'core/login.html')


def logout(request):
    auth.logout(request)
    return redirect ('/')