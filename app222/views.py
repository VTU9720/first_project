from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def raina(request):
    return HttpResponse('<marquee>raina is the best captain</marquee>')