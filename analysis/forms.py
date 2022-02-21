from django import forms
from . import models
from bootstrap_datepicker_plus.widgets import  DateTimePickerInput
from django.db.models.query import QuerySet
from .models import Analysis

class SamplePointForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # Call to ModelForm constructor
        for k in self.fields:
            self.fields[k].widget.attrs['style'] = 'width:250px;'
    class Meta:
        model = models.SamplePoint
        fields = ('name',)

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
        }

class AnalysisForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # Call to ModelForm constructor
        for k in self.fields:
            self.fields[k].widget.attrs['style'] = 'width:250px;'

    class Meta:
        model = models.Analysis
        fields = ('name', 'abbreviation','charge','molecular_weight')

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'abbreviation':forms.TextInput(attrs={'class':'form-control'}),
            'charge':forms.NumberInput(attrs={'class':'form-control'}),
            'molecular_weight':forms.NumberInput(attrs={'class':'form-control'}),
        }

class DateInput(forms.DateInput):
    input_type = 'datetime-local'

class TestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # Call to ModelForm constructor
        for k in self.fields:
            self.fields[k].widget.attrs['style'] = 'width:250px;'
    class Meta:
        model = models.Test
        fields=('lab_number', 'well', 'samplepoint', 'sampling_date', 'report_date')

        widgets={
            'lab_number':forms.TextInput(attrs={'class':'form-control'}),
            'well':forms.Select(attrs={'class':'form-control'}),
            'samplepoint':forms.Select(attrs={'class':'form-control'}),
            'sampling_date':DateTimePickerInput(),
            'report_date':DateTimePickerInput(),

        }

class TestAnalysis(forms.Form):

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        analysis = models.Analysis.objects.all()
        
        for item in analysis:
            self.fields[item.name] = forms.CharField(label=f'{item.name}({item.abbreviation})', max_length=10)
            self.fields[item.name].widget.attrs['class'] = 'form-control p-1'
            self.fields[item.name].widget.attrs['style'] = 'width:250px;'
   
   
class MetadataForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # Call to ModelForm constructor
        for k in self.fields:
            self.fields[k].widget.attrs['style'] = 'width:250px;'

    class Meta:
        model = models.MetaData
        fields = ('name',)

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
        }

class TestMetadata(forms.Form):

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        metadata = models.MetaData.objects.all()
        
        for item in metadata:
            self.fields[item.name] = forms.CharField(label=item.name, max_length=10)
            self.fields[item.name].widget.attrs['class'] = 'form-control p-1'
            self.fields[item.name].widget.attrs['style'] = 'width:250px;'

class StiffTemplateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # Call to ModelForm constructor
        for k in self.fields:
            self.fields[k].widget.attrs['style'] = 'width:250px;'
            self.fields[k].widget.attrs['class'] = 'form-control'

    class Meta:
        model = models.StiffTemplate
        fields = ('name',)

    
class StiffTemplateLevelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # Call to ModelForm constructor
        for k in self.fields:
            self.fields[k].widget.attrs['style'] = 'width:250px;'
            self.fields[k].widget.attrs['class'] = 'form-control'

    class Meta:
        model = models.StiffTemplateLevel
        fields = ('stiff_template','name',)


class StiffTemplateLevelIonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # Call to ModelForm constructor
        for k in self.fields:
            self.fields[k].widget.attrs['style'] = 'width:250px;'
            self.fields[k].widget.attrs['class'] = 'form-control'

    class Meta:
        model = models.StiffTemplateLevelIon
        fields = ('stiff_template_level','analysis',)