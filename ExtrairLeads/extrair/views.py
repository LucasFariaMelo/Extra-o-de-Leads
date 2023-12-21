from django.shortcuts import render, redirect
from .models import Lead
from .forms import LeadForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def lista_leads(request):
    leads = Lead.objects.all()
    return render(request, 'lista_leads.html', {'leads': leads})

def criar_lead(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_leads')
    else:
        form = LeadForm()
    return render(request, 'index.html', {'form': form})