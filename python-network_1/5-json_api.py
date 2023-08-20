#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


def main():

    allletter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': allletter}

    req = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        res = req.json()
        if res:
            print("[{}] {}".format(res['id'], res['name']))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    main()