from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Field(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.country.name + ', '+ self.name


class Well(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    easting = models.FloatField(null=True, blank=True)
    northing = models.FloatField(null=True, blank=True)
    utmzone = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_json(self):
        return {
            'field':self.field.name,
            'field_id':self.field.id,
            'name':self.name,
            'lat': self.lat,
            'long':self.long,
        }
