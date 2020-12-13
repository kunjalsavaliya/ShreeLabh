from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.


def home(request):
    return render(request, 'newshreelabh/index.html')