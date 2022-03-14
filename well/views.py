from django.shortcuts import render, redirect
from django.db.models import Count
from django.http import JsonResponse
from . import models
from . import forms
from django.contrib import messages
from analysis.models import Test, SamplePoint
from dataclasses import dataclass
from django.db.models import Count
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    context={}
    return render(request, 'well/dashboard.html', context)

@dataclass
class ModelItemsCount:
    title:str
    count:int
    url:str

@login_required
def loadDashboard(request):
    
    field_test = Test.objects.values('well__field__name').annotate(total=Count('id'))
    samplepoint_test = Test.objects.values('samplepoint__name').annotate(total=Count('id'))
    wells = models.Well.objects.all()
    summary=[
        ModelItemsCount('Tests',Test.objects.count(), 'test'),
        ModelItemsCount('Wells',models.Well.objects.count(), 'well'),
        ModelItemsCount('Fields',models.Field.objects.count(), 'field'),
        ModelItemsCount('Sample Points',SamplePoint.objects.count(), 'samplepoint'),
    ]

    context={
        'summary':summary,
        'field_test':field_test,
        'samplepoint_test':samplepoint_test,
        'wells':[item.get_json() for item in wells],
    }

    return render(request, 'well/dashboard.html', context)

@login_required
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


@login_required
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

@login_required
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

@login_required
def countryDelete(request, pk):
    
    country = models.Country.objects.get(id=pk)
    context = {'item':country}
    if request.method == "POST":
        country.delete()
        return redirect('country')
    
    return render(request,'delete.html', context)
    
@login_required
def wellLoad(request):
    wells = models.Well.objects.all()
    context = {'wells':wells}
    return render(request, 'well/well.html', context)

@login_required
def fieldLoad(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    if q=='':
        fields=models.Field.objects.all().annotate(c_count=Count('well'))
    else:
        fields=models.Field.objects.filter(country = int(q)).annotate(c_count=Count('well'))
        
    context={'fields':fields}
    return render(request,'well/field.html', context)

@login_required
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

@login_required
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

@login_required
def fieldDelete(request, pk):
    field = models.Field.objects.get(id=int(pk))
    context = {'item':field}
    if request.method == "POST":
        field.delete()
        return redirect('field')

    return render(request, 'delete.html', context)

@login_required
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

@login_required
def wellUpdate(request, pk):
    well = models.Well.objects.get(id=int(pk))
    form = forms.WellForm(instance=well)
    context={'form':form}
    if request.method == "POST":
        form = forms.WellForm(request.POST, instance=well)
        if form.is_valid():
            form.save()
            return redirect('well')
    return render(request, 'form.html', context)

@login_required
def wellDelete(request, pk):
    well = models.Well.objects.get(id=int(pk))
    context = {'item':well}
    if request.method == "POST":
        well.delete()
        return redirect('well')
        
    return render(request, 'delete.html', context)