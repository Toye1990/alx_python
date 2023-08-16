"""The request module imported to be used to fetch data"""
import requests
"""The request module imported to be used to fetch data"""
import sys
"""The request module imported to be used to fetch data"""

def request_email(url, email):
    """Sends a POST request to the given URL with the given email address as a parameter."""
    data = {'email': email}
    response = response.POST(url, email)
    return response.text

