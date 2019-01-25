#
# Copyright 2009 Optaros, Inc.
#
from django.contrib.gis.views import feed

from djalf.hierarchies.feeds import CategoryFeed
from djalf.hierarchies.models import Category, Hierarchy
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include, static
from djalf.alfresco import views as alfresco_views
from djalf.hierarchies import views as hierarchies_views
from django.views.generic import TemplateView

admin.autodiscover()

feeds = {
    "categories" : CategoryFeed,
}

urlpatterns = [
    #ADMIN
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/hierarchies/', include('djalf.hierarchies.urls')),
    url(r'^admin/alfresco/cache/', alfresco_views.cache, name='alfresco_cache'),
    url(r'^admin/(.*)', admin.site.urls, name='admin_home'),

    #ALFRESCO
    url(r'^alfresco/', include('djalf.alfresco.urls')),
    
    url(r'^site_map/$', TemplateView.as_view(template_name='site_map.html'), name='site_map'),
    url(r'^$', TemplateView.as_view(template_name='home.html'), {"template": "home.html"}, name='home'),
    
    
    url(r'^feeds/(?P<url>.*)/$', feed, {'feed_dict': feeds}),
    
    url(r'^(?P<slug>[-\w]+)/$', hierarchies_views.hierarchy_detail,
        {'queryset' : Hierarchy.objects.all(), 'slug_field' : 'slug'}, name='hierarchy_detail'),
    url(r'^(?P<path>.*)/content/(?P<id>[-\w]+)/$$', hierarchies_views.category_content_detail, name='category_content_detail'),
    url(r'^(?P<path>.*)/$', hierarchies_views.category_detail,
        {'queryset' : Category.objects.all(), 'slug_field' : 'slug'}, name='category_detail'),
    
] + static.static(r'^site_media/(?P<path>.*)$', document_root=settings.MEDIA_ROOT)