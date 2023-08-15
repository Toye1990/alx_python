"""The request module imported to be used to fetch data"""
import requests
"""The request module imported to be used to fetch data"""

def main():
 response = requests.get('https://alu-intranet.hbtn.io/status')
 if response.status == 200:
    print(response.content)
 else:
    print('error fetching status: {}'.format(response.status_code))