from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pagina_inicial'),
    path('criar_lead/', views.criar_lead, name='criar_lead'),
    path('leads/', views.lista_leads, name='lista_leads'),
]