from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

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