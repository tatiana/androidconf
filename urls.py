from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from core.views import handle_request

admin.autodiscover()

urlpatterns = patterns('',
                url(r'^admin/', include(admin.site.urls)),
                url(r'^order/', include('androidconf.orders.urls')),
                #url(r'^inscricao$', include('androidconf.products.urls')),
                url(r'^inscricao-cancelada$', handle_request, name='cancel_url'),
                url(r'^inscricao-confirmada$', handle_request, name='return_url'),
                url(r'^inscricao-', include('androidconf.products.urls')),
                (r'^something/hard/to/guess$', include('paypal.standard.ipn.urls')),
                (r'^.*$', handle_request),)

urlpatterns += staticfiles_urlpatterns()
