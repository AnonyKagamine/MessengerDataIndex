#!/usr/bin/python3
import sys
import json
from urllib.request import urljoin

GH_PAGES_PREFIX = "https://anonykagamine.github.io"
OUTPUT_FILENAME = "index.json"
def main():
    index_list = []
    for filename in sys.stdin.readlines():
        filename = filename.strip("\n")
        with open(filename, "r") as f:
            jsonobj = json.load(f)
            index_column = {}
            index_column["title"] = jsonobj["_title"]
            index_column["description"] = jsonobj["_description"]
            index_column["provider"] = jsonobj["_provider"]
            # index_column["url"] = urljoin(GH_PAGES_PREFIX, filename)
            index_column["url"] = "../" + filename

            index_list.append(index_column)

    with open(OUTPUT_FILENAME, "w") as f:
        json.dump(index_list, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    main()
