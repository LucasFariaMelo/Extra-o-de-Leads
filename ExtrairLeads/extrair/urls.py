from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_leads, name='lista_leads'),
]
