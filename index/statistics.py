from index.index import get_title
from index.index import tokenise_simple
import json



def number_documents(json_file):
    
    return len(json_file)



def number_token(json_file):

    total_token = 0
    for doc in json_file:
        total_token += len(tokenise_simple(get_title(doc)))

    return total_token



def number_token_median(json_file):

    documents = number_documents(json_file)
    tokens = number_token(json_file)
    
    return documents/tokens



def get_statistics(json_file):

    stats = {
        "number of documents": number_documents(json_file),
        "number of tokens": number_token(json_file)
    }
    stats["average of tokens per document"] = stats["number of tokens"]/stats["number of documents"]

    return stats



def write_statistics(stats):

    with open("metadata.json", "w") as f:
        json.dump(stats, f)
