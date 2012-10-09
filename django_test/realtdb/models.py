#-*- coding:utf-8 -*-

from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


class Realtor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)


class BaseApartment(models.Model):
    class Meta:
        # Please keep in mind that eventually future you might need to deal with other kinds of the real
        # estate like rooms, offices etc.
        abstract = True

    realtor = models.ForeignKey(Realtor, verbose_name=u'Realtor')
    address = models.CharField(u'Address', max_length=100)
    area = models.FloatField(u'Area (m^2)', help_text=u"In square meters")
    price = models.DecimalField(u'Price', max_digits=11, decimal_places=2)


class House(BaseApartment):
    pass


class Apartment(BaseApartment):
    rooms_num = models.PositiveSmallIntegerField(u'Number of rooms in apartment')
    floor = models.PositiveSmallIntegerField(u'Floor number', validators=[MinValueValidator(1)])
    floors_total = models.PositiveSmallIntegerField(u'Total number of floors in the apartment\'s building', validators=[MinValueValidator(1)])

    def clean(self):
        if self.floor > self.floors_total:
            raise ValidationError('Floor cannot be greater than total count of floors in building')


class Office(BaseApartment):
    business_centre = models.BooleanField(u'Is located in business centre')
