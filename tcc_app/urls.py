from django.urls import path
from . import views

urlpatterns = [ path("",views.home, name="HomePage"), path("filter", views.filter, name="Filtro")]