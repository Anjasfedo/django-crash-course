from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Speed'
    feature1.details = 'Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi'
    feature1.is_true = True
    
    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Im Birb'
    feature2.details = 'Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi'
    feature2.is_true = False
    
    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Lightning'
    feature3.details = 'Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi'
    feature3.is_true = True
    
    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Low'
    feature4.details = 'Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi'
    feature4.is_true = True
    
    feature5 = Feature()
    feature5.id = 4
    feature5.name = 'High'
    feature5.details = 'Voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi'
    feature5.is_true = False
    
    features = [feature1, feature2, feature3, feature4, feature5]
    
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