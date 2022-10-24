#!/usr/bin/python3
"""return a header value"""
import requests
import sys
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if 'X-Request-Id' in r.headers:
        print("{}".format(r.headers['X-Request-Id']))
