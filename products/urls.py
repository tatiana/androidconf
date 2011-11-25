from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    #url(r'^$', 'androidconf.products.views.product_detail_2nd', name='product_detail_2nd'),
    url(r'ultima-chamada$', 'androidconf.products.views.product_detail', name='product_detail'),
)

