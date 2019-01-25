#
# Copyright 2009 Optaros, Inc.
#
from django.conf.urls import url
from django.views.generic import TemplateView

from djalf.alfresco import views

urlpatterns = (
    url(r'login/$',  views.login, name='alfresco_login'),
    url(r'^logout/$',  views.logout, name='alfresco_logout'),
    url(r'^error/$',   TemplateView.as_view(template_name='error.html'), name='alfresco_error'),
    url(r'^ajax_search/$',   views.ajax_search, name='alfresco_ajax_search'),
    url(r'^static/(?P<id>[-\w]+)/$', views.static_content, name='static_detail'),
    url(r'^content/(?P<id>[-\w]+)/$',   views.content, name='content_detail'),
    url(r'^content/print_view/(?P<id>[-\w]+)/$', views.print_view, name='print_view'),
    url(r'^search/$',  views.search, name='search'),
    url(r'^tag_search/$', views.tag_search, name='tag_search'),
    url(r'^image/(?P<path>.*)', views.photo, name='image'),
)