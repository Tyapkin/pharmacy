from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('catalog.views',
    url(r'^$', 'index', name='index'),
    url(r'^catalog/$', 'catalog', name='catalog'),
    url(r'^search/$', 'search', name='search'),
    url(r'^drug/(?P<uid>\d+)/$', 'drug_detail', name='drug_detail'),
)
