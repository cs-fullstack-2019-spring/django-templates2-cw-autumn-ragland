from django.urls import path
from . import views

# paths triggered in html files
urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:movie_ID>', views.details, name='details'),
    path('synop/<int:movie_ID>', views.synop, name='synop'),
]
