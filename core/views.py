from django.shortcuts import render_to_response

def homepage(request):
    from django.conf import settings
    context = {'STATIC_URL': settings.STATIC_URL}
    return render_to_response('index.html', context)
