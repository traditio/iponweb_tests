#-*- coding:utf-8 -*-

from decimal import Decimal
import random

from django.shortcuts import render, redirect

from realtdb.forms import HouseForm
from realtdb.models import Realtor, House


def house_list(request):
    if request.method == "POST":
        random_realtor = random.choice(Realtor.objects.all())
        f = HouseForm(request.POST)
        if f.is_valid():
            new_house = f.save(commit=False)
            new_house.realtor = random_realtor
            new_house.save()
            return redirect(request.path)
    else:
        f = HouseForm()

    house_list = House.objects.select_related().order_by('-id')
    return render(request, "realtdb/houses.html", {'house_list': house_list, 'form': f})
