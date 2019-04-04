from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from site_app.models import Guest
from django.contrib.auth.mixins import LoginRequiredMixin
from site_app.forms import GuestForm

# Create your views here.
class IndexView(TemplateView):
    template_name = 'site_app/index.html'

class GuestListView(ListView):
    context_object_name = 'guests'

    model = Guest

    # guest list

class GuestDetailView(DetailView):
    context_object_name = 'guest_detail'
    model = Guest
    template_name = 'site_app/guest_detail.html'


class GuestCreateView(CreateView, LoginRequiredMixin):
    login_url = '/login/'

    redirect_field_name = 'site_app/guest_detail.html'

    form_class = GuestForm

    model = Guest
