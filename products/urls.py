from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'$', 'androidconf.products.views.product_detail', name='product_detail'),
)

