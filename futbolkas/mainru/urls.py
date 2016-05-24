from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('',
                       url(r'^$', 'mainru.views.home'),
                       url(r'^ru/item/(?P<alias>[^/]+)', 'mainru.views.item'),
                       url(r'^ru/order/', 'mainru.views.order'),
                       url(r'^(?P<alias>[^/]+)', 'mainru.views.get_category'),

                       )
