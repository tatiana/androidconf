from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'$', 'androidconf.orders.views.success_order', name='return_url'),
    url(r'$', 'androidconf.orders.views.cancel_order', name='cancel_url'),
)

