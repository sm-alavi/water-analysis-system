# Generated by Django 4.0.2 on 2022-03-03 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('well', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='well',
            name='easting',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='well',
            name='northing',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='well',
            name='utmzone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
