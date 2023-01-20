from index import index_json
from index import tokenise_simple
from index import write_index



def main(json_file, tokenise):

    write_index(index_json(json_file, tokenise))



if __name__ == '__main__':

    main("crawled_urls_json", tokenise_simple)