#from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Temperature
User = get_user_model()


class TemperatureListView(LoginRequiredMixin, ListView):
    model = Temperature

class TemperatureDetailView(LoginRequiredMixin, DetailView):
    model = Temperature

class TemperatureUpdateView(LoginRequiredMixin, CreateView):
    fields = ['temp',]
    model = Temperature