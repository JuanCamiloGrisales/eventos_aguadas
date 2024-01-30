from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = SignUpForm()

    return render(request, 'register.html' , {'form': form})

def logout(request):
    logout(request)
    return redirect('home')