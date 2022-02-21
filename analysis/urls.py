from django.urls import path
from . import views

urlpatterns = [
    path('analysis/', views.analysisLoad, name='analysis'),
    path('analysis-create/', views.analysisCreate, name='analysis-create'),
    path('analysis-update/<str:pk>', views.analysisUpdate, name='analysis-update'),
    path('analysis-delete/<str:pk>', views.analysisDelete, name='analysis-delete'),

    path('samplepoint/', views.samplepointLoad, name='samplepoint'),
    path('samplepoint-create/', views.samplepointCreate, name='samplepoint-create'),
    path('samplepoint-update/<str:pk>', views.samplepointUpdate, name='samplepoint-update'),
    path('samplepoint-delete/<str:pk>', views.samplepointDelete, name='samplepoint-delete'),

    path('test/', views.testLoad, name='test'),
    path('testview/<str:pk>', views.testView, name='test-view'),
    path('test-create/', views.testCreate, name='test-create'),
    path('test-update/<str:pk>', views.testUpdate, name='test-update'),
    path('test-delete/<str:pk>', views.testDelete, name='test-delete'),

    path('metadata/', views.metadataLoad, name='metadata'),
    path('metadata-create/', views.metadataCreate, name='metadata-create'),
    path('metadata-update/<str:pk>', views.metadataUpdate, name='metadata-update'),
    path('metadata-delete/<str:pk>', views.metadataDelete, name='metadata-delete'),
    
    path('testanalysis-modify/<str:pk>', views.testanalysisModify, name='testanalysis-modify'),
    path('testmetadata-modify/<str:pk>', views.testmetadataModify, name='testmetadata-modify'),

    path('stifftemplate/', views.stifftemplateLoad, name='stifftemplate'),
    path('stifftemplate/<str:pk>', views.stifftemplateLoad, name='stifftemplate-view'),
    path('stifftemplate-create/', views.stifftemplateCreate, name='stifftemplate-create'),
    path('stifftemplate-update/<str:pk>', views.samplepointUpdate, name='stifftemplate-update'),
    path('stifftemplate-delete/<str:pk>', views.samplepointDelete, name='stifftemplate-delete'),

    path('stifftemplatelevel/<str:pk>', views.stifftemplateLoad, name='stifftemplatelevel'),

]
