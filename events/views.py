from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def main_events(request):
    return HttpResponse("<h1>Hello from event page</h1>")