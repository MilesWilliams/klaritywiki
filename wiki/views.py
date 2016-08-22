from .models import Website, Categories
from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View


# Create your views here.


class IndexView(generic.ListView):
    template_name = 'wiki/index.html'
    context_object_name = 'website_list'

    def get_queryset(self):
        return Website.objects.all()

class DetailView(generic.DetailView):
    model = Categories
    template_name = 'wiki/detail.html'

class AlbumUpdate(UpdateView):
    model = Categories
    fields =['title','text']
