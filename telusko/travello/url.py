from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculator', views.calculator, name='home'),
    path('add', views.displayResult, name='add'),
]