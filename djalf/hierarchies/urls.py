#
# Copyright 2009 Optaros, Inc.
#
from django.conf.urls import url
from django.urls import include

from djalf.hierarchies import views

urlpatterns = (
       url(r'^category/(?P<id>\d+)/order/$', views.category_order),
       url(r'^hierarchy/(?P<id>\d+)/order/$', views.hierarchy_subcategory_order),
       url(r'^hierarchy/order/$', views.hierarchy_order),
)