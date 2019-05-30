from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

simple_get('https://www.oregon.gov/odva/Benefits/Pages/Education.aspx')
response = simple_get('https://www.oregon.gov/odva/Benefits/Pages/Education.aspx')
education_html = BeautifulSoup(response, 'html.parser')
with open('education_html.txt', 'w', encoding='utf-8') as f:
    for p in education_html.select('p'):
        print(p.text)
        f.write(p.text)
    for panel_title in education_html.select('.panel-title'):
        print(panel_title.text)
        f.write(panel_title.text)

simple_get('https://www.oregon.gov/odva/Benefits/Pages/Employment.aspx')
response = simple_get('https://www.oregon.gov/odva/Benefits/Pages/Employment.aspx')
employment_html = BeautifulSoup(response, 'html.parser')
with open('employment_html.txt', 'w', encoding='utf-8') as f:
    for p in employment_html.select('p'):
        print(p.text)
        f.write(p.text)
    for panel_title in employment_html.select('.panel-title'):
        print(panel_title.text)
        f.write(panel_title.text)

simple_get('https://www.oregon.gov/odva/Benefits/Pages/How-to-File-a-Claim.aspx')
response = simple_get('https://www.oregon.gov/odva/Benefits/Pages/How-to-File-a-Claim.aspx')
claims_process_html = BeautifulSoup(response, 'html.parser')
with open('claims_process_html.txt', 'w', encoding='utf-8') as f:
    for p in claims_process_html.select('p'):
        print(p.text)
        f.write(p.text)
    for panel_title in claims_process_html.select('.panel-title'):
        print(panel_title.text)
        f.write(panel_title.text)

simple_get('https://www.oregon.gov/odva/Benefits/Pages/Disability-Compensation.aspx')
response = simple_get('https://www.oregon.gov/odva/Benefits/Pages/Disability-Compensation.aspx')
disability_compensation_html = BeautifulSoup(response, 'html.parser')
with open('disability_compensation_html.txt', 'w', encoding='utf-8') as f:
    for p in disability_compensation_html.select('p'):
        print(p.text)
        f.write(p.text)
    for panel_title in disability_compensation_html.select('.panel-title'):
        print(panel_title.text)
        f.write(panel_title.text)

simple_get('https://www.oregon.gov/odva/Benefits/Pages/Emergency-Assistance.aspx')
response = simple_get('https://www.oregon.gov/odva/Benefits/Pages/Emergency-Assistance.aspx')
emergency_assistance_html = BeautifulSoup(response, 'html.parser')
with open('emergency_assistance_html.txt', 'w', encoding='utf-8') as f:
    for p in emergency_assistance_html.select('p'):
        print(p.text)
        f.write(p.text)
    for panel_title in emergency_assistance_html.select('.panel-title'):
        print(panel_title.text)
        f.write(panel_title.text)

simple_get('https://www.oregon.gov/odva/Benefits/Pages/Home-Loans.aspx')
response = simple_get('https://www.oregon.gov/odva/Benefits/Pages/Home-Loans.aspx')
home_loans_html = BeautifulSoup(response, 'html.parser')
with open('home_loans_html.txt', 'w', encoding='utf-8') as f:
    for p in home_loans_html.select('p'):
        print(p.text)
        f.write(p.text)
    for panel_title in home_loans_html.select('.panel-title'):
        print(panel_title.text)
        f.write(panel_title.text)

simple_get('https://www.oregon.gov/odva/Benefits/Pages/Records-Medals.aspx')
response = simple_get('https://www.oregon.gov/odva/Benefits/Pages/Records-Medals.aspx')
records_medals_html = BeautifulSoup(response, 'html.parser')
with open('records_medals_html.txt', 'w', encoding='utf-8') as f:
    for p in records_medals_html.select('p'):
        print(p.text)
        f.write(p.text)
    for panel_title in records_medals_html.select('.panel-title'):
        print(panel_title.text)
        f.write(panel_title.text)

simple_get('https://www.oregon.gov/odva/Benefits/Pages/Licenses.aspx')
response = simple_get('https://www.oregon.gov/odva/Benefits/Pages/Licenses.aspx')
license_plates_html = BeautifulSoup(response, 'html.parser')
with open('license_plates_html.txt', 'w', encoding='utf-8') as f:
    for p in license_plates_html.select('p'):
        print(p.text)
        f.write(p.text)
    for panel_title in license_plates_html.select('.panel-title'):
        print(panel_title.text)
        f.write(panel_title.text)

simple_get('https://www.oregon.gov/odva/Benefits/Pages/Veteran-IDs.aspx')
response = simple_get('https://www.oregon.gov/odva/Benefits/Pages/Veteran-IDs.aspx')
veteran_IDs_html = BeautifulSoup(response, 'html.parser')
with open('veteran_IDs_html.txt', 'w', encoding='utf-8') as f:
    for p in veteran_IDs_html.select('p'):
        print(p.text)
        f.write(p.text)
    for panel_title in veteran_IDs_html.select('.panel-title'):
        print(panel_title.text)
        f.write(panel_title.text)

simple_get('https://www.oregon.gov/odva/Benefits/Pages/Burial.aspx')
response = simple_get('https://www.oregon.gov/odva/Benefits/Pages/Burial.aspx')
burial_benefits_html = BeautifulSoup(response, 'html.parser')
with open('burial_benefits_html.txt', 'w', encoding='utf-8') as f:
    for p in burial_benefits_html.select('p'):
        print(p.text)
        f.write(p.text)
    for panel_title in burial_benefits_html.select('.panel-title'):
        print(panel_title.text)
        f.write(panel_title.text)

simple_get('https://www.oregon.gov/odva/Benefits/Pages/Healthcare.aspx')
response = simple_get('https://www.oregon.gov/odva/Benefits/Pages/Healthcare.aspx')
health_html = BeautifulSoup(response, 'html.parser')
with open('health_html.txt', 'w', encoding='utf-8') as f:
    for p in health_html.select('p'):
        print(p.text)
        f.write(p.text)
    for panel_title in health_html.select('.panel-title'):
        print(panel_title.text)
        f.write(panel_title.text)

simple_get('https://www.oregon.gov/odva/Benefits/Pages/Long-Term-Care.aspx')
response = simple_get('https://www.oregon.gov/odva/Benefits/Pages/Long-Term-Care.aspx')
long_term_care_html = BeautifulSoup(response, 'html.parser')
with open('long_term_care_html.txt', 'w', encoding='utf-8') as f:
    for p in long_term_care_html.select('p'):
        print(p.text)
        f.write(p.text)
    for panel_title in long_term_care_html.select('.panel-title'):
        print(panel_title.text)
        f.write(panel_title.text)

simple_get('https://www.oregon.gov/odva/Benefits/Pages/Pension.aspx')
response = simple_get('https://www.oregon.gov/odva/Benefits/Pages/Pension.aspx')
pension_html = BeautifulSoup(response, 'html.parser')
with open('pension_html.txt', 'w', encoding='utf-8') as f:
    for p in pension_html.select('p'):
        print(p.text)
        f.write(p.text)
    for panel_title in pension_html.select('.panel-title'):
        print(panel_title.text)
        f.write(panel_title.text)

simple_get('https://www.oregon.gov/odva/Benefits/Pages/Recreation.aspx')
response = simple_get('https://www.oregon.gov/odva/Benefits/Pages/Recreation.aspx')
recreation_html = BeautifulSoup(response, 'html.parser')
with open('recreation_html.txt', 'w', encoding='utf-8') as f:
    for p in recreation_html.select('p'):
        print(p.text)
        f.write(p.text)
    for panel_title in recreation_html.select('.panel-title'):
        print(panel_title.text)
        f.write(panel_title.text)

simple_get('https://www.oregon.gov/odva/Benefits/Pages/Special-Advocacy.aspx')
response = simple_get('https://www.oregon.gov/odva/Benefits/Pages/Special-Advocacy.aspx')
special_advocacy_html = BeautifulSoup(response, 'html.parser')
with open('special_advocacy_html.txt', 'w', encoding='utf-8') as f:
    for p in special_advocacy_html.select('p'):
        print(p.text)
        f.write(p.text)
    for panel_title in special_advocacy_html.select('.panel-title'):
        print(panel_title.text)
        f.write(panel_title.text)

simple_get('https://www.oregon.gov/odva/Benefits/Pages/Taxes.aspx')
response = simple_get('https://www.oregon.gov/odva/Benefits/Pages/Taxes.aspx')
taxes_html = BeautifulSoup(response, 'html.parser')
with open('taxes_html.txt', 'w', encoding='utf-8') as f:
    for p in taxes_html.select('p'):
        print(p.text)
        f.write(p.text)
    for panel_title in taxes_html.select('.panel-title'):
        print(panel_title.text)
        f.write(panel_title.text)

simple_get('https://www.oregon.gov/odva/Benefits/Pages/Transportation.aspx')
response = simple_get('https://www.oregon.gov/odva/Benefits/Pages/Transportation.aspx')
transportation_html = BeautifulSoup(response, 'html.parser')
with open('transportation_html.txt', 'w', encoding='utf-8') as f:
    for p in transportation_html.select('p'):
        print(p.text)
        f.write(p.text)
    for panel_title in transportation_html.select('.panel-title'):
        print(panel_title.text)
        f.write(panel_title.text)

simple_get('https://www.oregon.gov/odva/Benefits/Pages/Vet-Owned-Business.aspx')
response = simple_get('https://www.oregon.gov/odva/Benefits/Pages/Vet-Owned-Business.aspx')
veteran_owned_businesses_html = BeautifulSoup(response, 'html.parser')
with open('veteran_owned_businesses_html.txt', 'w', encoding='utf-8') as f:
    for p in veteran_owned_businesses_html.select('p'):
        print(p.text)
        f.write(p.text)
    for panel_title in veteran_owned_businesses_html.select('.panel-title'):
        print(panel_title.text)
        f.write(panel_title.text)

simple_get('https://www.oregon.gov/odva/Benefits/Pages/Volunteer-Program.aspx')
response = simple_get('https://www.oregon.gov/odva/Benefits/Pages/Volunteer-Program.aspx')
veteran_volunteer_program_html = BeautifulSoup(response, 'html.parser')
with open('veteran_volunteer_program_html.txt', 'w', encoding='utf-8') as f:
    for p in veteran_volunteer_program_html.select('p'):
        print(p.text)
        f.write(p.text)
    for panel_title in veteran_volunteer_program_html.select('.panel-title'):
        print(panel_title.text)
        f.write(panel_title.text)








#tags = soup.find_all("li", "panel-title")
