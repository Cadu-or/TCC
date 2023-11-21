from django.urls import path
from . import views

urlpatterns = [ 
    path("",views.home, name="HomePage"), 
    path("filter", views.filter, name="Filtro"),
    path("filterhome/<str:indicador1>/<str:indicador2>/<str:delay>", views.filterhome, name='FilterHome'),

]