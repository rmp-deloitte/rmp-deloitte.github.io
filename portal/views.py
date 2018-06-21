from django.shortcuts import render
from .models import Application

# Create your views here.
def index(request):
    apps = Application.objects.all()
    return render(request, 'portal/index.html', {"apps" : apps})
