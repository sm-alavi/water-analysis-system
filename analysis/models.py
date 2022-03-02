from django.db import models
from well.models import Well

# Create your models here.

class SamplePoint(models.Model):
    name = models.CharField(max_length=200)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    
class Analysis(models.Model):
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=50, null=True, blank=True)
    charge = models.IntegerField(null=True, blank=True)
    molecular_weight = models.FloatField(null=True, blank=True)
    equivalent_weight = models.FloatField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + (self.abbreviation)
    
    @property
    def eqv_weight(self):
        return self.molecular_weight/abs(self.charge)


class Test(models.Model):
    lab_number = models.CharField(max_length=200)
    samplepoint = models.ForeignKey(SamplePoint, on_delete=models.DO_NOTHING)
    well = models.ForeignKey(Well, on_delete=models.CASCADE)
    sampling_date = models.DateTimeField()
    report_date = models.DateTimeField(blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lab_number

    def get_json(self):
        return {
            'id': self.id, 
            'lab_number': self.lab_number,
            'sampling_date':self.sampling_date,
            'report_date':self.report_date,
            'created':self.created,
            'updated':self.updated,
            'well':[
                {
                    'id':self.well.id,
                    'name':self.well.name,
                    'field':self.well.field.name
                }
            ],
            'analysis':[
                {
                    'id':item.id,
                    'name':item.analysis.name,
                    'analysis_id':item.analysis.id,
                    'abbreviation':item.analysis.abbreviation,
                    'value':item.value,
                    'meqv':item.meqv,
                }

                for item in self.testanalysis_set.all()
            ]

        }


class TestAnalysis(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE)
    value = models.FloatField(null=True, blank=True)

    @property
    def meqv(self):
        return self.value/self.analysis.eqv_weight


class MetaData(models.Model):
    name=models.CharField(max_length=200)
    unit=models.CharField(max_length=50, null=True, blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class TestMetadata(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    metadata = models.ForeignKey(MetaData, on_delete=models.CASCADE)
    value = models.FloatField(null=True, blank=True)

class StiffTemplate(models.Model):
    name = models.CharField(max_length=200)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class StiffTemplateLevel(models.Model):
    stiff_template = models.ForeignKey(StiffTemplate, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class StiffTemplateLevelIon(models.Model):
    stiff_template_level = models.ForeignKey(StiffTemplateLevel, on_delete=models.CASCADE, related_name='stifftemplatelevelions')
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    


