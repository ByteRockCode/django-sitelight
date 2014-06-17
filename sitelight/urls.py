from django.conf.urls import patterns, url


urlpatterns = patterns('sitelight.views',
    url(r'^$', 'index'),
    url(r'^sitemap.xml?$', 'sitemap'),
    url(r'^(?P<slug>[a-zA-Z0-9-]+)/?$', 'page'),
    url(r'^(?P<category>[a-zA-Z0-9-]+)/(?P<entry>[a-zA-Z0-9-]+)/?$', 'entry'),
)
