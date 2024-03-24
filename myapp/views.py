from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    features = Feature.objects.all()
    
    context = {
        'features': features,
    }
    
    return render(request, 'index.html', context)

def counter(request):
    words = request.POST['words']
    
    context = {
        'amount_of_words': len(words.split())
    }
    
    return render(request, 'counter.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeat_password = request.POST['repeatPassword']

        if password != repeat_password:
            messages.info(request, 'Password not same')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email is exist')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username is exist')
            return redirect('register')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save();
        
        return redirect('login')
    
    return render(request, 'register.html')