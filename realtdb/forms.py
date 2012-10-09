from django.forms import ModelForm, ValidationError
from realtdb.models import House, Apartment, Office


class HouseForm(ModelForm):
    class Meta:
        model = House
        exclude = ('realtor',)


class ApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        exclude = ('realtor',)


class OfficeForm(ModelForm):
    class Meta:
        model = Office
        exclude = ('realtor',)