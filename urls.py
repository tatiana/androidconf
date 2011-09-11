from django.conf.urls.defaults import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core.views import handle_request 

urlpatterns = patterns('',
                 (r'^.*$', handle_request),)

urlpatterns += staticfiles_urlpatterns()
