from index.index import index_json
from index.index import tokenise_simple
from index.index import write_index
from index.index import open_json

from index.statistics import get_statistics
from index.statistics import write_statistics



def main(json_file, tokenise):

    index = index_json(json_file, tokenise)
    write_index(index)
    write_statistics(get_statistics(index))



if __name__ == '__main__':

    main("crawled_urls.json", tokenise_simple)