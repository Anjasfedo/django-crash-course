from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # name = 'Anjas'
    context = {
        'name': 'Anjas',
        'age': 21
    }
    return render(request, 'index.html', context)
