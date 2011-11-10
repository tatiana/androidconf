from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

template = {"sobre": "index.html",
            "local": "place.html",
            "patrocine": "sponsor.html",
            "inscricao": "registration.html",
            "inscricao-confirmada": "success.html",
            "inscricao-cancelada": "cancel.html",
            "programacao": "agenda.html"}

def handle_request(request):
    page = request.path.split('/')[-1]
    if page not in template:
        page = "sobre"
    context = {'STATIC_URL': settings.STATIC_URL, 'current_page': page}
    return render_to_response(template[page], context)



