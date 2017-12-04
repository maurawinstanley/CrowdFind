# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Item
from .forms import ItemForm

# Create your views here.
def found(request):
    entry_list = Item.objects.filter(status="Found")
    c = {
        'entry_list': entry_list
    }
    return render(request, 'found.html', c)

def lost(request):
    entry_list = Item.objects.filter(status="Lost")
    c = {
        'entry_list': entry_list
    }
    return render(request, 'lost.html', c)

def postItem(request):
    if request.POST:
        form = ItemForm(request.POST)

        if form.is_valid():
            form.save()
            form = ItemForm()
            args = {}
            args['form'] = form
            return HttpResponseRedirect('/login/main/', args)
        else:
            form = ItemForm()

        args = {}
        args['form'] = form
        return render(request, 'postItem.html', args)
    
    else:
        form = ItemForm()
        args = {}
        args['form'] = form
        return render(request, 'postItem.html', args)