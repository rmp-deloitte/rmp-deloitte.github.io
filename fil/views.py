from django.shortcuts import render
from .models import Inmate
from .forms import InmateForm

# Create your views here.
def index(request):
    return render(request, 'fil/index.html', { 'inmates' : Inmate.objects.all() })

def results(request):
    return render(request, 'fil/results/fil-results-index.html', {})
