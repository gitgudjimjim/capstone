from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#def basetemplate(request):
#    return render(request, 'capapp/basetemplate.html')
def index(request):
    return render(request, 'capapp/index.html')
def ap(request):
    return render(request, 'capapp/adaptive_programs.html')
def claims(request):
    return render(request, 'capapp/claims_process.html')
def disability(request):
    return render(request, 'capapp/disability_compensation_and_pensions.html')
def education(request):
    return render(request, 'capapp/education.html')
def employment(request):
    return render(request, 'capapp/employment.html')
def homeless(request):
    return render(request, 'capapp/homelessness_and_emergency.html')
def housing(request):
    return render(request, 'capapp/housing_and_property_tax.html')
def IDs(request):
    return render(request, 'capapp/IDs_DMVplates_records.html')
def justice(request):
    return render(request, 'capapp/justice_involved_veterans.html')
def longterm(request):
    return render(request, 'capapp/long_term_care.html')
def medical(request):
    return render(request, 'capapp/medical_and_mental_health.html')
def vethomes(request):
    return render(request, 'capapp/oregon_veteran_homes.html')
def recreation(request):
    return render(request, 'capapp/recreation.html')
def advocacy(request):
    return render(request, 'capapp/special_advocacy.html')
def care(request):
    return render(request, 'capapp/specialty_care.html')
def survivor(request):
    return render(request, 'capapp/survivor_and_family_benefits.html')
def transportation(request):
    return render(request, 'capapp/transportation.html')
def trauma(request):
    return render(request, 'capapp/trauma.html')
def businesses(request):
    return render(request, 'capapp/veteran_owned_businesses.html')
def service(request):
    return render(request, 'capapp/working_with_a_veteran_service_officer.html')


# def <view name>(request):
#    context = {<name-value pairs>}
#    return render(request, '<app name>/<template name>.html', context)
