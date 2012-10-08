from django.forms import ModelForm, ValidationError
from apartments.models import Apartment


class ApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        exclude = ('realtor',)

    def clean(self):
        cleaned_data = super(ApartmentForm, self).clean()
        floor = cleaned_data.get("floor")
        floors_total = cleaned_data.get("floors_total")

        # Only do something if both fields are valid so far.
        if floor and floors_total and floor > floors_total:
            raise ValidationError("Floor number cannot be greater than total numbers of floors in building")

        # Always return the full collection of cleaned data.
        return cleaned_data