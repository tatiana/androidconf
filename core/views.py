from django.conf import settings
from django.shortcuts import render_to_response

template = {"sobre": "index.html",
            "local": "place.html",
            "inscricao": "under-construction.html",
            "programacao": "under-construction.html"}

def handle_request(request):
    page = request.path.split('/')[-1]
    if page not in template:
        page = "sobre"
    context = {'STATIC_URL': settings.STATIC_URL, 'current_page': page}
    return render_to_response(template[page], context)
