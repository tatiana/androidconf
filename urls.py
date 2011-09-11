from django.conf.urls.defaults import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core.views import about, place, subscribe, schedule

urlpatterns = patterns('',
                 (r'^index$', about),
                 (r'^sobre$', about),
                 (r'^local$', place),
                 (r'^inscricao$', subscribe),
                 (r'^programacao$', schedule),
                 (r'^$', about),
                 (r'^.*$', about),)

urlpatterns += staticfiles_urlpatterns()
