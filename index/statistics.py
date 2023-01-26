from index.index import get_title
from index.index import tokenise_simple
import json



def number_documents(dict):
    
    nb_doc = 0
    doc_visited = []
    for key in dict.keys():
        for doc in dict[key]:
            if doc not in doc_visited:
                nb_doc += 1
                doc_visited.append(doc)
    return nb_doc



def number_token(dict):

    return len(dict.keys())



def get_statistics(dict):

    stats = {
        "number of documents": number_documents(dict),
        "number of tokens": number_token(dict)
    }
    if stats["number of documents"] != 0:
        stats["average of tokens per document"] = stats["number of tokens"]/stats["number of documents"]


    return stats



def write_statistics(stats):

    with open("metadata.json", "w") as f:
        json.dump(stats, f)
