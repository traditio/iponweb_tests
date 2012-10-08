from django.forms import ModelForm
from realtdb.models import House


class HouseForm(ModelForm):
    class Meta:
        model = House
        exclude = ('realtor',)