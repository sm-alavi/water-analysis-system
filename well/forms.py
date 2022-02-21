from django.forms import ModelForm, TextInput, Select, Textarea
from django import forms
from . import models

class CountryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # Call to ModelForm constructor
        for k in self.fields:
            self.fields[k].widget.attrs['style'] = 'width:250px;'

    class Meta:
        model = models.Country
        fields = ('name',)

        widgets={
            'name': TextInput(attrs={'class':'form-control'}), 
        }

class FieldForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # Call to ModelForm constructor
        for k in self.fields:
            self.fields[k].widget.attrs['style'] = 'width:250px;'
            self.fields[k].widget.attrs['class'] = 'form-control'

    class Meta:
        model = models.Field
        fields = ('country','name')

 


class WellForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # Call to ModelForm constructor
        for k in self.fields:
            self.fields[k].widget.attrs['style'] = 'width:250px;'
            
    class Meta:
        model = models.Well
        fields=('field', 'name', )

        widgets={
            'field': Select(attrs={'class':'form-control'}),
            'name':TextInput(attrs={'class':'form-control'}),
        }