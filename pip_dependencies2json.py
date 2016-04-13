import json
import sys

import re


def parse(content):
    libs = []
    for line in content:
        match = re.match("^([^=]+)==(.+)$", line)
        if match:
            libs.append({
                "type": "pip",
                "name": match.groups()[0],
                "version": match.groups()[1]
            })

    return libs


if __name__ == '__main__':
    print(json.dumps(parse(sys.stdin), indent=4, sort_keys=True))
