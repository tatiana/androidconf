from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'$', 'products.views.product_detail', name='product_detail'),
)

