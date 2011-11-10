import uuid
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from androidconf.products.models import Product

class PayPalForm(PayPalPaymentsForm):
    def get_image(self):
        return "%simg/button-paypal.gif" % settings.STATIC_URL

def product_detail(request, slug="androidconf-2011-wl"):
    product = get_object_or_404(Product, slug=slug)
    paypal = {
        'amount': product.price,
        'item_name': product.title,
        'item_number': product.slug,
        # PayPal wants a unique invoice ID
        'invoice': str(uuid.uuid1()),
        # It'll be a good idea to setup a SITE_DOMAIN inside settings
        # so you don't need to hardcode these values.
        "notify_url": "%s%s" % (settings.SITE_DOMAIN, reverse('paypal-ipn')),
        'return_url': settings.SITE_DOMAIN + reverse('return_url'),
        'cancel_return': settings.SITE_DOMAIN + reverse('cancel_url'),
        'currency_code': 'BRL',
        'lc': 'BR',
    }
    form = PayPalForm(initial=paypal)
    if settings.DEBUG:
        rendered_form = form.sandbox()
    else:
        rendered_form = form.render()
    return render_to_response('registration_waiting_list.html', {
        'product' : product,
        'form' : rendered_form,
        'current_page': 'inscricao'
    }, RequestContext(request))

