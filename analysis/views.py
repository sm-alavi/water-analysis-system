from contextlib import redirect_stderr
from random import sample
from django.shortcuts import render, redirect
from django.http import JsonResponse
from . import forms
from . import models
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Create your views here.

def analysisLoad(request):
    analysis = models.Analysis.objects.all()
    context={'analysis':analysis}

    return render(request, 'analysis/analysis.html', context)

def analysisCreate(request):
    form = forms.AnalysisForm()
    
    if request.method == "POST":
        form = forms.AnalysisForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('analysis')
    context = {'form':form}      
    return render(request, 'form.html', context)

def analysisUpdate(request, pk):
    analysis = models.Analysis.objects.get(id=int(pk))
    form = forms.AnalysisForm(instance=analysis)
    if request.method == "POST":
        form = forms.AnalysisForm(request.POST, instance=analysis)
        if form.is_valid:
            form.save()
            return redirect('analysis')
    context={'form':form}

    return render(request, 'form.html', context)

def analysisDelete(request, pk):
    analysis = models.Analysis.objects.get(id=int(pk))
    analysis.delete()
    return redirect('analysis')


def samplepointLoad(request):
    samplepoint = models.SamplePoint.objects.all()
    context={'samplepoint':samplepoint}
    return render(request, 'analysis/samplepoint.html', context)

def samplepointCreate(request):
    form = forms.SamplePointForm()
    if request.method == "POST":
        form = forms.SamplePointForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('samplepoint')
    context={'form':form}
    return render(request, 'form.html', context)

def samplepointUpdate(request, pk):
    samplepoint = models.SamplePoint.objects.get(id=int(pk))
    form = forms.SamplePointForm(instance=samplepoint)
    if request.method == "POST":
        form = forms.SamplePointForm(request.POST, instance=samplepoint)
        if form.is_valid:
            form.save()
            return redirect('samplepoint')
    context={'form':form}
    return render(request, 'form.html', context)

def samplepointDelete(request, pk):
    samplepoint = models.SamplePoint.objects.get(id=int(pk))
    samplepoint.delete()
    return redirect('samplepoint')

def testLoad(request):
    test = models.Test.objects.all()
    context={'test':test}
    return render(request, 'analysis/test.html', context)

def testCreate(request):
    form = forms.TestForm()
    if request.method=="POST":
        form=forms.TestForm(request.POST)
        form.save()
        return redirect('test')
    context={'form':form}
    return render(request, 'form.html', context)

def testUpdate(request, pk):
    test=models.Test.objects.get(id=int(pk))
    form=forms.TestForm(instance=test)
    if request.method=="POST":
        form=forms.TestForm(request.POST, instance=test)
        if form.is_valid:
            form.save()
            return redirect('form')
    context={'form':form}
    return render(request, 'form.html', context)

def testDelete(request, pk):
    test = models.Test.objects.get(id=int(pk))
    test.delete()
    return redirect('test')
    
def testView(request, pk):
    test=models.Test.objects.get(id=int(pk))

    testanalysis = models.TestAnalysis.objects.filter(test=test)
    testmetadata = models.TestMetadata.objects.filter(test=test)
    context={
        'test':test,
        'testanalysis':testanalysis,
        'testmetadata':testmetadata
    }
    return render(request, 'analysis/testview.html',context)

def testanalysisModify(request, pk):
    testanalysis = models.TestAnalysis.objects.filter(test=int(pk))
    initials = {item.analysis.name:item.value for item in testanalysis}
    form = forms.TestAnalysis(initial=initials)
    analysis = models.Analysis.objects.all()
    if request.method=="POST":
        form = forms.TestAnalysis(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            for item in analysis:
                val = data[item.name]
                try:
                    testanalysis = models.TestAnalysis.objects.get(Q(test=int(pk)) & Q(analysis = int(item.id)))
                    testanalysis.value = val
                    testanalysis.save()
                except ObjectDoesNotExist:
                    p = models.TestAnalysis(test=models.Test.objects.get(id = int(pk)), analysis=models.Analysis.objects.get(id = int(item.id)), value = val )
                    p.save(force_insert=True)
            return redirect('test')
            
    context={'form':form}
    return render(request, 'form.html', context)


def metadataLoad(request):
    metadata = models.MetaData.objects.all()
    context={'metadata':metadata}

    return render(request, 'analysis/metadata.html', context)

def metadataCreate(request):
    form = forms.MetadataForm()
    
    if request.method == "POST":
        form = forms.MetadataForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('metadata')
    context = {'form':form}      
    return render(request, 'form.html', context)

def metadataUpdate(request, pk):
    metadata = models.MetaData.objects.get(id=int(pk))
    form = forms.MetadataForm(instance=metadata)
    if request.method == "POST":
        form = forms.MetadataForm(request.POST, instance=metadata)
        if form.is_valid:
            form.save()
            return redirect('metadata')
    context={'form':form}

    return render(request, 'form.html', context)

def metadataDelete(request, pk):
    metadata = models.MetaData.objects.get(id=int(pk))
    metadata.delete()
    return redirect('metadata')   

def testmetadataModify(request, pk):
    testmetadata = models.TestMetadata.objects.filter(test=int(pk))
    initials = {item.metadata.name:item.value for item in testmetadata}
    form = forms.TestMetadata(initial=initials)
    metadata = models.MetaData.objects.all()
    if request.method=="POST":
        form = forms.TestMetadata(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            for item in metadata:
                val = data[item.name]
                try:
                    testmetadata = models.TestMetadata.objects.get(Q(test=int(pk)) & Q(metadata = int(item.id)))
                    testmetadata.value = val
                    testmetadata.save()
                except ObjectDoesNotExist:
                    p = models.TestMetadata(test=models.Test.objects.get(id = int(pk)), metadata=models.MetaData.objects.get(id = int(item.id)), value = val )
                    p.save(force_insert=True)
            return redirect('test')
            
    context={'form':form}
    return render(request, 'form.html', context)


def stifftemplateLoad(request):
    stifftemplate = models.StiffTemplate.objects.all()
    context = {'data':stifftemplate}
    return render(request, 'analysis/stifftemplate.html', context)

def stifftemplateCreate(request):
    form = forms.StiffTemplateForm()
    if request.method=="POST":
        form = forms.StiffTemplateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stifftemplate')
    context = {'form':form}
    return render(request, 'form.html', context)


def stifftemplateUpdate(request, pk):
    stifftemplate = models.StiffTemplate.objects.get(id=int(pk))
    form = forms.StiffTemplateForm(instance=stifftemplate)
    if request.method=="POST":
        form = forms.StiffTemplateForm(request.POST, instance = stifftemplate)
        if form.is_valid():
            form.save()
            messages.success(request, f"{str(request.POST.get('name')).title()} updated succesfully.")
            return redirect('stifftemplate')
    context = {'form':form}
    return render(request, 'form.html', context)

def stifftemplateDelete(request, pk):
    stifftemplate = models.StiffTemplate.objects.get(id=int(pk))
    stifftemplate.delete()
    messages.success(request, f"{stifftemplate.name.title()} deleted succesfully.")
    return redirect('stifftemplate')

def stifftemplatelevelLoad(request, pk):
    stifftemplate = models.StiffTemplate.objects.get(id=int(pk))
    stifftemplatelevel = models.StiffTemplateLevel.objects.filter(stiff_template=stifftemplate)
    context = {
        'data':stifftemplatelevel,
        'stifftemplate':stifftemplate}

    return render(request, 'analysis/stifftemplatelevel.html', context)

def stifftemplatelevelCreate(request, pk):
    form = forms.StiffTemplateLevelForm(initial={'stiff_template':int(pk)})
    if request.method=="POST":
        form = forms.StiffTemplateLevelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stifftemplatelevel', pk=str(pk))
    context = {'form':form}
    return render(request, 'form.html', context)

def stifftemplatelevelUpdate(request, pk):
    stifftemplatelevel = models.StiffTemplateLevel.objects.get(id=int(pk))
    idp = stifftemplatelevel.stiff_template_id
    form = forms.StiffTemplateLevelForm(instance = stifftemplatelevel)
    if request.method=="POST":
        form = forms.StiffTemplateLevelForm(request.POST,instance = stifftemplatelevel)
        if form.is_valid():
            form.save()
            return redirect('stifftemplatelevel', pk=str(idp))
    context = {'form':form}
    return render(request, 'form.html', context)

def stifftemplatelevelDelete(request, pk):
    stifftemplatelevel = models.StiffTemplateLevel.objects.get(id=int(pk))
    pid = stifftemplatelevel.stiff_template_id
    stifftemplatelevel.delete()
    messages.success(request, f"{stifftemplatelevel.name.title()} deleted succesfully.")
    return redirect('stifftemplatelevel', pk=pid)


def stifftemplatelevelionLoad(request, pk):
    stifftemplatelevel= models.StiffTemplateLevel.objects.get(id=int(pk))
    stifftemplatelevelion = models.StiffTemplateLevelIon.objects.filter(stiff_template_level_id=stifftemplatelevel)
    context = {
        'data':stifftemplatelevelion,
        'stifftemplatelevel':stifftemplatelevel}

    return render(request, 'analysis/stifftemplatelevelion.html', context)


def stifftemplatelevelionCreate(request, pk):
    form = forms.StiffTemplateLevelIonForm(initial={'stiff_template_level':int(pk)})
    if request.method=="POST":
        form = forms.StiffTemplateLevelIonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stifftemplatelevelion', pk=str(pk))
    context = {'form':form}
    return render(request, 'form.html', context)

def stifftemplatelevelionDelete(request, pk):
    stifftemplatelevelion= models.StiffTemplateLevelIon.objects.get(id=int(pk))
    pid = stifftemplatelevelion.stiff_template_level_id
    stifftemplatelevelion.delete()
    messages.success(request, f"{stifftemplatelevelion.analysis.name.title()} deleted succesfully.")
    return redirect('stifftemplatelevelion', pk=pid)

def createNote(request):
    tests = models.Test.objects.all()
    context={'test':tests}
    if request.method == 'POST': 
        test_id = request.POST.get('test_id') 
        test = models.Test.objects.get(id=int(test_id))
        return JsonResponse({'test_data':test}) 

    return render(request, 'analysis/radar.html', context)