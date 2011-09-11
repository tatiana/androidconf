from django.conf.urls.defaults import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core.views import about, place, subscribe, schedule

urlpatterns = patterns('',
                 (r'^index.html$', about),
                 (r'^sobre.html$', about),
                 (r'^local.html$', place),
                 (r'^inscricao.html$', subscribe),
                 (r'^programacao.html$', schedule),
                 (r'^$', about),
                 (r'^.*$', about),)

urlpatterns += staticfiles_urlpatterns()
