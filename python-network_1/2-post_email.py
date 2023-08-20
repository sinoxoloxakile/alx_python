#!/usr/bin/python3
"""
    Write a Python script that takes in a URL and an email address,
    sends a POST request to the passed URL with the email as a parameter,
"""
import requests
import sys


def main():
    """
        take arguments data and url and make request
    """
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    res = requests.post(url, data)

    print(res.text)


if __name__ == "__main__":
    main()