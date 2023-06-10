from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    sequenz = Sequenz.objects.filter()
    context = {
        'sequenz': sequenz,
    }
    return render(request, 'planApp1/plan.html', context)