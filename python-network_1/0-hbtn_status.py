"""The request module imported to be used to fetch data"""
import requests
"""The request module imported to be used to fetch data"""
def res(text):
 response = requests.get('https://alu-intranet.hbtn.io/status')
 return response.text

 