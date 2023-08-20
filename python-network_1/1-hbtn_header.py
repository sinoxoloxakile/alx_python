#!/usr/bin/python3

'''
    Write a Python script that takes in a URL and an email address,
    sends a POST request to the passed
    URL with the email as a parameter, and
    finally displays the body of the response.
'''

import requests
import sys

def main():
    r = sys.argv[1]
    """
    The email must be sent in the variable email
    """
    res = requests.get(r)
    if 'X-Request-Id' in res.headers:
        print(res.headers['X-Request-Id'])
    else:
        return None

if __name__ == "__main__":
    main()