from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'$', 'orders.views.success_order', name='return_url'),
    url(r'$', 'orders.views.cancel_order', name='cancel_url'),
)

