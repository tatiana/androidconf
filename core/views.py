from django.conf import settings
from django.shortcuts import render_to_response

def about(request):
    context = {'STATIC_URL': settings.STATIC_URL}
    return render_to_response('index.html', context)

def place(request):
    context = {'STATIC_URL': settings.STATIC_URL}
    return render_to_response('place.html', context)

def subscribe(request):
    context = {'STATIC_URL': settings.STATIC_URL}
    return render_to_response('under-construction.html', context)

def schedule(request):
    context = {'STATIC_URL': settings.STATIC_URL}
    return render_to_response('under-construction.html', context)
