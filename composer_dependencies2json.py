import json
import sys

import re


def parse(content):
    libs = []
    for line in content:
        match = re.match("^(\S+/\S+)\s+([\S]+)\s+.*", line)
        if match:
            libs.append({
                "type": "composer",
                "name": match.groups()[0],
                "version": match.groups()[1]
            })

    return libs


if __name__ == '__main__':
    print(json.dumps(parse(sys.stdin), indent=4, sort_keys=True))
