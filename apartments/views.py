import random

from django.shortcuts import redirect, render

from apartments.forms import ApartmentForm
from apartments.models import Apartment
from realtdb.models import Realtor


def apartments_list(request):
    if request.method == "POST":
        random_realtor = random.choice(Realtor.objects.all())
        form = ApartmentForm(request.POST)
        if form.is_valid():
            new_house = form.save(commit=False)
            new_house.realtor = random_realtor
            new_house.save()
            return redirect(request.path)
    else:
        form = ApartmentForm()

    apartments = Apartment.objects.select_related().order_by('-id')
    return render(request, "apartments/apartments.html", {'apartments': apartments, 'form': form})

