from urllib import request
from bs4 import BeautifulSoup as BS



def get_title(url):

    url_request = request.urlopen(url)
    soup = BS(url_request, 'html.parser')

    return soup.title.text


def tokenise_simple(title):

    return title.split(" ")