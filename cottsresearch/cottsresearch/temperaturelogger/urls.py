from django.urls import path
from . import views

app_name = "temperaturelogger"


urlpatterns = [
    path(
        route='',
        view=views.TemperatureListView.as_view(),
        name='list'
    ),
    path(
        route='<int:pk>/',
        view=views.TemperatureDetailView.as_view(),
        name='detail'
    )
]
