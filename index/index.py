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



def add_token_index(index, token, doc):

    if token in index.keys():
        index[token].append(doc)
    
    else:
        index[token] = [doc]



def index_doc(index, doc):

    tokens = tokenise_simple(get_title(doc))
    for token in tokens:
        add_token_index(index, token, doc)



def index_json(json_file):
    
    index = dict()
    data = open_json(json_file)

    for elt in data:
        index_doc(index, elt)
    
    return index



def write_index(index):
    
    with open("title.non_pos_index.json", "w") as f:
        json.dump(index,f)