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
#tags = soup.find_all("li", "panel-title")
