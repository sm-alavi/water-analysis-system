from django.urls import path
from . import views

urlpatterns = [
    path('', views.loadDashboard, name='dashboard'),
    path('country/', views.countryLoad, name='country'),
    path('country/<str:pk>', views.countryLoad, name='country'),
    path('wells/', views.wellLoad, name='well'),
    path('fields/', views.fieldLoad, name='field'),

    path('country_create/', views.countryCreate, name='country-create'),
    path('country_update/<str:pk>', views.countryUpdate, name='country-update'),
    path('country_delete/<str:pk>', views.countryDelete, name='country-delete'),

    path('field_create/', views.fieldCreate, name='field-create'),
    path('field_create/<str:pk>', views.fieldCreate, name='field-create'),
    path('field_update/<str:pk>', views.fieldUpdate, name='field-update'),
    path('field_delete/<str:pk>', views.fieldDelete, name='field-delete'),

    path('well_create/', views.wellCreate, name='well-create'),
    path('well_create/<str:pk>', views.wellCreate, name='well-create'),
    path('well_update/<str:pk>', views.wellUpdate, name='well-update'),
    path('well_delete/<str:pk>', views.wellDelete, name='well-delete'),



]
