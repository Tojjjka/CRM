from django.shortcuts import render, get_object_or_404, redirect
from .models import Company, Client
from .forms import CompanyForm, ClientForm


def index(request):
    return render(request, 'crm/index.html')


# ---------- Компании ----------
def company_list(request):
    companies = Company.objects.all()
    return render(request, 'crm/company_list.html', {'companies': companies})


def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'crm/company_form.html', {'form': form, 'title': 'Добавить компанию'})


def company_edit(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'crm/company_form.html', {'form': form, 'title': 'Редактировать компанию'})


def company_delete(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        company.delete()
        return redirect('company_list')
    return render(request, 'crm/company_confirm_delete.html', {'company': company})


# ---------- Клиенты ----------
def client_list(request):
    clients = Client.objects.select_related('company').all()
    return render(request, 'crm/client_list.html', {'clients': clients})


def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'crm/client_form.html', {'form': form, 'title': 'Добавить клиента'})


def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'crm/client_form.html', {'form': form, 'title': 'Редактировать клиента'})


def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'crm/client_confirm_delete.html', {'client': client})
