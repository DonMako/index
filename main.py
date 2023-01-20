from index.index import index_json
from index.index import tokenise_simple
from index.index import write_index



def main(json_file, tokenise):

    write_index(index_json(json_file, tokenise))



if __name__ == '__main__':

    main("urls_tests.json", tokenise_simple)