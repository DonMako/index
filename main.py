from index.index import index_json
from index.index import tokenise_simple
from index.index import write_index

from index.statistics import get_statistics
from index.statistics import write_statistics



def main(json_file, tokenise):

    write_index(index_json(json_file, tokenise))
    write_statistics(get_statistics(json_file))



if __name__ == '__main__':

    main("urls_tests.json", tokenise_simple)