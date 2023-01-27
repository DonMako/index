from index.index import index_json
from index.index import index_json_stem
from index.index import tokenise_simple
from index.index import write_index
from index.index import write_index_stem

from index.statistics import get_statistics
from index.statistics import write_statistics
from index.statistics import write_statistics_stem



def main(json_file, tokenise):

    index = index_json(json_file, tokenise)
    write_index(index)
    index_stem = index_json_stem(json_file, tokenise)
    write_index_stem(index_stem)
    write_statistics(get_statistics(index))
    write_statistics_stem(get_statistics(index_stem))



if __name__ == '__main__':

    main("crawled_urls.json", tokenise_simple)