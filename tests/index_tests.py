import index.index as index

def test_open_json():

    return ( type(index.open_json("crawled_json")) == list )

