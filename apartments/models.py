#-*- coding:utf-8 -*-

from django.db import models
from realtdb.models import Realtor


class BaseApartment(models.Model):
    class Meta:
        # Please keep in mind that eventually future you might need to deal with other kinds of the real
        # estate like rooms, offices etc.
        abstract = True

    realtor = models.ForeignKey(Realtor)
    address = models.CharField(max_length=100)
    area = models.FloatField(help_text=u"In square meters")
    price = models.DecimalField(max_digits=11, decimal_places=2)


class Apartment(BaseApartment):
    rooms_num = models.PositiveSmallIntegerField(u'Number of rooms in apartment')
    floor = models.PositiveSmallIntegerField(u'Floor number')
    floors_total = models.PositiveSmallIntegerField(u'Total number of floors in the apartment\'s building')
