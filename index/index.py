from urllib import request
from bs4 import BeautifulSoup as BS
import json



def open_json(json_file):

    with open(json_file, "r") as f:
        data = json.load(f)
    
    return data



def get_title(url):

    title = " "
    
    try:
        url_request = request.urlopen(url)
        soup = BS(url_request, 'html.parser')
        title = soup.title.text

    except:
        pass

    return title



def tokenise_simple(title):

    return title.split(" ")



def 

    with open("metadata.json", "w") as f:
        json.dump(stats, f)




def write_index(index):
    
    with open("title.non_pos_index.json", "w") as f:
        json.dump(index,f)