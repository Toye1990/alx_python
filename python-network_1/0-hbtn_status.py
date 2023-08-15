import requests

def main():
 response = requests.get('https://alu-intranet.hbtn.io/status')
 if response.status == 200:
    print(response.content)
 else:
    print('error fetching status: {}'.format(response.status_code))