from django.urls import path
from django.views.generic.base import TemplateView
from . import views

app_name = 'capapp' # for namespacing
urlpatterns = [
    path('', views.homepage, name='homepage'),
    #path('', TemplateView.as_view(template_name='capapp/homepage.html'), name='homepage'),
    #path('homepage', TemplateView.as_view(template_name='capapp/homepage.html'), name='homepage'),
    path('ap', TemplateView.as_view(template_name='capapp/adaptive_programs.html'), name='adaptive_programs'),
    path('burial_benefits', TemplateView.as_view(template_name='capapp/burial_benefits.html'), name='burial_benefits'),
    path('claims', TemplateView.as_view(template_name='capapp/claims_process.html'), name='claims_process'),
    path('disability', TemplateView.as_view(template_name='capapp/disability_compensation.html'), name='disability_compensation'),
    path('education', TemplateView.as_view(template_name='capapp/education.html'), name='education'),
    path('employment', TemplateView.as_view(template_name='capapp/employment.html'), name='employment'),
    path('emergency', TemplateView.as_view(template_name='capapp/emergency_assistance.html'), name='emergency_assistance'),
    path('home_loans', TemplateView.as_view(template_name='capapp/home_loans.html'), name='home_loans'),
    path('records_medals', TemplateView.as_view(template_name='capapp/records_medals.html'), name='records_medals'),
    path('license_plates', TemplateView.as_view(template_name='capapp/license_plates.html'), name='license_plates'),
    path('justice', TemplateView.as_view(template_name='capapp/justice_involved_veterans.html'), name='justice_involved_veterans'),
    path('longterm', TemplateView.as_view(template_name='capapp/long_term_care.html'), name='long_term_care'),
    path('health', TemplateView.as_view(template_name='capapp/health_care.html'), name='health'),
    path('pension', TemplateView.as_view(template_name='capapp/pension.html'), name='pension'),
    path('taxes', TemplateView.as_view(template_name='capapp/taxes.html'), name='taxes'),
    path('vethomes', TemplateView.as_view(template_name='capapp/oregon_veteran_homes.html'), name='oregon_veteran_homes'),
    path('veteran_IDs', TemplateView.as_view(template_name='capapp/veteran_IDs.html'), name='veteran_IDs'),
    path('veteran_volunteer_program', TemplateView.as_view(template_name='capapp/veteran_volunteer_program.html'), name='veteran_volunteer_program'),
    path('recreation', TemplateView.as_view(template_name='capapp/recreation.html'), name='recreation'),
    path('advocacy', TemplateView.as_view(template_name='capapp/special_advocacy.html'), name='special_advocacy'),
    path('care', TemplateView.as_view(template_name='capapp/specialty_care.html'), name='specialty_care'),
    path('survivor', TemplateView.as_view(template_name='capapp/survivor_and_family_benefits.html'), name='survivor_and_family_benefits'),
    path('transportation', TemplateView.as_view(template_name='capapp/transportation.html'), name='transportation'),
    path('trauma', TemplateView.as_view(template_name='capapp/trauma.html'), name='trauma'),
    path('businesses', TemplateView.as_view(template_name='capapp/veteran_owned_businesses.html'), name='veteran_owned_businesses'),
    path('service', TemplateView.as_view(template_name='capapp/working_with_a_veteran_service_officer.html'), name='working_with_a_veteran_service_officer'),


]
