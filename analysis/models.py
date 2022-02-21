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
    abbreviation = models.CharField(max_length=50, null=True)
    charge = models.IntegerField(null=True)
    molecular_weight = models.FloatField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + (self.abbreviation)


class Test(models.Model):
    lab_number = models.CharField(max_length=200)
    samplepoint = models.ForeignKey(SamplePoint, on_delete=models.DO_NOTHING)
    well = models.ForeignKey(Well, on_delete=models.CASCADE)
    sampling_date = models.DateTimeField()
    report_date = models.DateTimeField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lab_number


class TestAnalysis(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE)
    value = models.FloatField(null=True)



class MetaData(models.Model):
    name=models.CharField(max_length=200)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class TestMetadata(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    metadata = models.ForeignKey(MetaData, on_delete=models.CASCADE)
    value = models.FloatField(null=True)

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
    stiff_template_level = models.ForeignKey(StiffTemplateLevel, on_delete=models.CASCADE)
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    


