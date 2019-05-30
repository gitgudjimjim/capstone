from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#def basetemplate(request):
#    return render(request, 'capapp/basetemplate.html')
def homepage(request):
    return render(request, 'capapp/homepage.html')
def ap(request):
    return render(request, 'capapp/adaptive_programs.html')
def burial_benefits(request):
    return render(request, 'capapp/burial_benefits.html')
def claims(request):
    return render(request, 'capapp/claims_process.html')
def disability(request):
    return render(request, 'capapp/disability_compensation_and_pensions.html')
def education(request):
    return render(request, 'capapp/education.html')
def employment(request):
    return render(request, 'capapp/employment.html')
def emergency(request):
    return render(request, 'capapp/emergency_assistance.html')
def home_loans(request):
    return render(request, 'capapp/home_loans.html')
def license_plates(request):
    return render(request, 'capapp/license_plates.html')
def records_medals(request):
    return render(request, 'capapp/records_medals.html')
def justice(request):
    return render(request, 'capapp/justice_involved_veterans.html')
def longterm(request):
    return render(request, 'capapp/long_term_care.html')
def health(request):
    return render(request, 'capapp/health_care.html')
def pension(request):
    return render(request, 'capapp/pension.html')
def taxes(request):
    return render(request, 'capapp/taxes.html')
def vethomes(request):
    return render(request, 'capapp/oregon_veteran_homes.html')
def veteran_IDs(request):
    return render(request, 'capapp/veteran_IDs.html')
def veteran_volunteer_program(request):
    return render(request, 'capapp/veteran_volunteer_program.html')
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
