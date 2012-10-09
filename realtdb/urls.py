#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url
from realtdb.forms import HouseForm, ApartmentForm, OfficeForm
urlpatterns = patterns('realtdb.views',
    url('^houses/$', 'house_list', kwargs={'form_cls': HouseForm, 'template': 'houses'}, name="realtdb-houses"),
    url('^apartments/$', 'house_list', kwargs={'form_cls': ApartmentForm, 'template': 'apartments'}, name="realtdb-apartments"),
    url('^offices/$', 'house_list', kwargs={'form_cls': OfficeForm, 'template': 'offices'}, name="realtdb-offices"),
)
