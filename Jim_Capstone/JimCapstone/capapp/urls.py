from django.urls import path
from django.views.generic.base import TemplateView
from . import views

app_name = 'capapp' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('ap', TemplateView.as_view(template_name='capapp/adaptive_programs.html'), name='adaptive_programs'),
    path('claims', TemplateView.as_view(template_name='capapp/claims_process.html'), name='claims_process'),
    path('disability', TemplateView.as_view(template_name='capapp/disability_compensation_and_pensions.html'), name='disability_compensation'),
    path('education', TemplateView.as_view(template_name='capapp/education.html'), name='education'),
    path('employment', TemplateView.as_view(template_name='capapp/employment.html'), name='employment'),
    path('homeless', TemplateView.as_view(template_name='capapp/homelessness_and_emergency.html'), name='homelessness_and_emergency'),
    path('housing', TemplateView.as_view(template_name='capapp/housing_and_property_tax.html'), name='housing_and_property_tax'),
    path('IDs', TemplateView.as_view(template_name='capapp/IDs_DMVplates_records.html'), name='IDs_DMVplates_records'),
    path('justice', TemplateView.as_view(template_name='capapp/justice_involved_veterans.html'), name='justice_involved_veterans'),
    path('longterm', TemplateView.as_view(template_name='capapp/long_term_care.html'), name='long_term_care'),
    path('medical', TemplateView.as_view(template_name='capapp/medical_and_mental_health.html'), name='medical_and_mental_health'),
    path('vethomes', TemplateView.as_view(template_name='capapp/oregon_veteran_homes.html'), name='oregon_veteran_homes'),
    path('recreation', TemplateView.as_view(template_name='capapp/recreation.html'), name='recreation'),
    path('advocacy', TemplateView.as_view(template_name='capapp/special_advocacy.html'), name='special_advocacy'),
    path('care', TemplateView.as_view(template_name='capapp/specialty_care.html'), name='specialty_care'),
    path('survivor', TemplateView.as_view(template_name='capapp/survivor_and_family_benefits.html'), name='survivor_and_family_benefits'),
    path('transportation', TemplateView.as_view(template_name='capapp/transportation.html'), name='transportation'),
    path('trauma', TemplateView.as_view(template_name='capapp/trauma.html'), name='trauma'),
    path('businesses', TemplateView.as_view(template_name='capapp/veteran_owned_businesses.html'), name='veteran_owned_businesses'),
    path('service', TemplateView.as_view(template_name='capapp/working_with_a_veteran_service_officer.html'), name='working_with_a_veteran_service_officer'),


]
