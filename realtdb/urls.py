#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from realtdb.forms import HouseForm, ApartmentForm, OfficeForm

house_list = {'form_cls': HouseForm, 'template': 'houses'}

urlpatterns = patterns('realtdb.views',
    url('^$', 'house_list', kwargs=house_list, name="home"),
    url('^houses/$', 'house_list', kwargs=house_list, name="realtdb-houses"),
    url('^apartments/$', 'house_list', kwargs={'form_cls': ApartmentForm, 'template': 'apartments'}, name="realtdb-apartments"),
    url('^offices/$', 'house_list', kwargs={'form_cls': OfficeForm, 'template': 'offices'}, name="realtdb-offices"),
)
