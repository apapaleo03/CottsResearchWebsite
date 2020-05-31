from django.urls import path
from . import views

app_name = "temperaturelogger"


urlpatterns = [
    path(
        route='',
        view=views.TemperatureListView.as_view(),
        name='list'
    ),
]
