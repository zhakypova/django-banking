from django.shortcuts import render, get_object_or_404


from django.views import generic

from .models import Credit, Client, Account


class IndexView(generic.ListView):
    model = Client
    template_name = 'index.html'
    context_object_name = 'clients'

class DetailClient(generic.DetailView):
    model = Client
    template_name = 'detail.html'
    context_object_name = 'client'


