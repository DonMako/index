from index import get_title
from index import tokenise


def number_documents(json_file):
    
    return len(json_file)



def number_token(url):

    return len(tokenise(get_title(url)))



def number_token_median(json_file):

    total_token = 0
    for doc in json_file:
        total_token += number_token(doc)
    
    return number_documents/total_token



def most_represented_token(json_file):

    dict = {}
    for url in json_file:
        tokens = tokenise(get_title(url))
        for token in tokens:
            
            if token not in dict:
                dict[token] = 1
            
            else:
                dict[token] += 1
    

