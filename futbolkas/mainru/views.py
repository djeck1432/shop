from django.shortcuts import render
from .models import *
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string

from django.http import HttpResponse, Http404
from django.template.loader import render_to_string

from .models import *


def home(request):
    category = Categoryru.objects.all()
    context = {

        'title': ' Souvenir4you',
        'categories': category,

    }
    return HttpResponse(render_to_string("souvenirru.html", context))


def item(request, alias):
    try:
        tovar = Itemru.objects.get(alias=alias)
    except:
        raise ('Not Found ')
    context = {

        'tovar': tovar,

    }
    return HttpResponse(render_to_string("itemru.html", context))


def get_category(request, alias):
    try:
        category = Categoryru.objects.get(alias=alias)
        tovars = Itemru.objects.filter(category=category)
    except:
        raise ('Not Found')
    context = {

        'tovars': tovars,
        'category': category,

    }
    return HttpResponse(render_to_string("itemru.html", context))


def order(request):
    context = {
    }
    return HttpResponse(render_to_string("korsina.html", context))
