from django.shortcuts import render
from .models import Lead

# Create your views here.

def lista_leads(request):
    leads = Lead.objects.all()
    return render(request, 'lista_leads.html', {'leads': leads})
