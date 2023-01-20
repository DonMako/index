import json
import pandas as pd
from index import tokenise_simple



def main(json_file, tokenise):

    df = pd.read_json(json_file)
    print(df)


if __name__ == '__main__':
    main("crawled_urls_json", tokenise_simple)