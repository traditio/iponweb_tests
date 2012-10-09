#-*- coding:utf-8 -*-
import random

from django.shortcuts import render, redirect

from realtdb.models import Realtor


def house_list(request, form_cls, template):
    if request.method == "POST":
        random_realtor = random.choice(Realtor.objects.all())
        f = form_cls(request.POST)
        if f.is_valid():
            obj = f.save(commit=False)
            obj.realtor = random_realtor
            obj.save()
            return redirect(request.path)
    else:
        f = form_cls()
    objects = form_cls.Meta.model.objects.select_related().order_by('-id')
    return render(request, "realtdb/{}.html".format(template), {'objects': objects, 'form': f})
