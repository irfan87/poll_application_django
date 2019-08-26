from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    message = "If you see this message, that means you are good to go!"
    return HttpResponse(message)
