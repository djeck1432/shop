from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string
from django.views.generic import CreateView

from .models import *


def home(request):
    category = Category.objects.all()
    context = {

        'title': ' Souvenir4you',
        'categories': category,

    }
    return HttpResponse(render_to_string("souviner.html", context))


def item(request, alias):
    try:
        tovar = Item.objects.get(alias=alias)
    except Item.DoesNotExist:
        raise Http404('Not Found ')
    context = {

        'tovar': tovar,

    }
    return HttpResponse(render_to_string("item.html", context))


def get_category(request, alias):
    try:
        category = Category.objects.get(alias=alias)
        tovars = Item.objects.filter(category=category)
    except Category.DoesNotExist:
        return Http404('Not Found')
    context = {

        'tovars': tovars,
        'category': category,

    }
    return HttpResponse(render_to_string("item.html", context))


def order(request):
    context = {
    }
    return HttpResponse(render_to_string("korsina.html", context))


class PaysCreateView(CreateView):
    model = Forma
    fields = '__all__'
    template_name = "pay_form.html"
    success_url = "/souvenir4you/"
