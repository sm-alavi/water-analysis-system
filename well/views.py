from django.shortcuts import render, redirect
from django.db.models import Count
from django.http import JsonResponse
from . import models
from . import forms
from django.contrib import messages
from analysis.models import Test, SamplePoint
from dataclasses import dataclass

# Create your views here.
def home(request):
    context={}
    return render(request, 'well/dashboard.html', context)

@dataclass
class ModelItemsCount:
    title:str
    count:int
    url:str

def loadDashboard(request):

    if not request.user.is_authenticated:
        return redirect('login')
    
    summary=[
        ModelItemsCount('Tests',Test.objects.count(), 'test'),
        ModelItemsCount('Wells',models.Well.objects.count(), 'well'),
        ModelItemsCount('Fields',models.Field.objects.count(), 'field'),
        ModelItemsCount('Sample Points',SamplePoint.objects.count(), 'samplepoint'),
    ]

    context={
        'summary':summary
    }

    return render(request, 'well/dashboard.html', context)

def countryLoad(request, pk=None):

    countries = models.Country.objects.all().annotate(c_count=Count('field'))
    form = forms.CountryForm()
    country=None
    if pk is not None:
        country = models.Country.objects.get(id=pk)
    if request.method == "POST":
        if "edit" in request.POST:
            country=country

        elif "delete" in request.POST:
            country.delete()
            return redirect('country')

        else:
            form = forms.CountryForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('country')
    

    context={
        'country_single':country, 
        'country':countries, 
        'form':form
    }

    return render(request, 'well/country.html', context)



def countryUpdate(request, pk=None):
    if request.method=="POST":
        if pk is not None:
            name = request.POST.get("name")
            country = models.Country.objects.get(id=int(pk))
            country.name = name
            country.save()
            country._meta.app_label
            country.__class__.__name__
            return redirect('country')

    return redirect('country')

def countryCreate(request):
    form = forms.CountryForm()
    if request.method=="POST":
        form = forms.CountryForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, f"{str(request.POST.get('name')).title()} added succesfully.")
            return redirect('country')

    context={'form':form}
    return render(request, 'form.html', context)

def countryDelete(request, pk):
    
    country = models.Country.objects.get(id=pk)
    country.delete()
    return redirect('country')
    

def wellLoad(request):
    wells = models.Well.objects.all()
    context = {'wells':wells}
    return render(request, 'well/well.html', context)

def fieldLoad(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    if q=='':
        fields=models.Field.objects.all().annotate(c_count=Count('well'))
    else:
        fields=models.Field.objects.filter(country = int(q)).annotate(c_count=Count('well'))
        
    context={'fields':fields}
    return render(request,'well/field.html', context)


def fieldCreate(request, pk=None):
    form = forms.FieldForm(initial={'country':pk})
    if request.method == "POST":
        form = forms.FieldForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, f"{str(request.POST.get('name')).title()} added succesfully.")
            return redirect('field')
    context={'form':form}
    return render(request, 'form.html', context)

def fieldUpdate(request, pk):
    field = models.Field.objects.get(id=int(pk))
    form = forms.FieldForm(instance=field)
    context={'form':form}
    if request.method == "POST":
        form = forms.FieldForm(request.POST, instance=field)
        if form.is_valid():
            form.save()
            return redirect('field')
    return render(request, 'form.html', context)
    
def fieldDelete(request, pk):
    field = models.Field.objects.get(id=int(pk))
    field.delete()
    return redirect('field')

def wellCreate(request, pk=None):
    form = forms.WellForm(initial={'field':pk})
    
    if request.method == "POST":
        form = forms.WellForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, f"{str(request.POST.get('name')).title()} added succesfully.")
            return redirect('well')
    context={'form':form}
    return render(request, 'form.html', context)

def wellUpdate(request, pk):
    well = models.Well.objects.get(id=int(pk))
    form = forms.WellForm(instance=well)
    context={'form':form}
    if request.method == "POST":
        well = forms.WellForm(request.POST, instance=well)
        if form.is_valid():
            form.save()
            return redirect('field')
    return render(request, 'form.html', context)

def wellDelete(request, pk):
    well = models.Well.objects.get(id=int(pk))
    well.delete()
    return redirect('well')