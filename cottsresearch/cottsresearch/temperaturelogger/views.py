#from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from .models import Temperature
#User

class TemperatureListView(LoginRequiredMixin, ListView):
    model = Temperature

class TemperatureDetailView(LoginRequiredMixin, DetailView):
    model = Temperature

class TemperatureCreateView(LoginRequiredMixin, CreateView):
    fields = ['temp',]
    model = Temperature

    def form_valid(self, form):
        #member = get_object_or_404(self.request.user)
        form.instance.member = self.request.user
        return super(TemperatureCreateView,self).form_valid(form)