from django.conf.urls.defaults import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core.views import homepage

urlpatterns = patterns('',
                 (r'^$', homepage),
)

urlpatterns += staticfiles_urlpatterns()
