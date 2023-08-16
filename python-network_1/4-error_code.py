"""The request module imported to be used to fetch data"""
import requests
"""The request module imported to be used to fetch data"""
import sys
"""The request module imported to be used to fetch data"""

def display_now(url):
    response = response.get(url)
    if response.status_code >= 400:
        print(response.status_code)
    else:
        print(response.text)
