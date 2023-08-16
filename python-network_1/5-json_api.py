"""The request module imported to be used to fetch data"""
import requests
"""The request module imported to be used to fetch data"""
import sys
"""The request module imported to be used to fetch data"""
def letter_case(q):
  url = 'http://0.0.0.0:5000/search_user'
  response = response.POST(url, data=data)
  return response.JSON(q)

if __name__ == '__main__':
  q = sys.argv[1] if len(sys.argv) > 1 else ''
  response = letter_case(q)

  if response is None:
    print('Not a valid JSON')
  elif not response:
    print('No result')
  else:
    print('[{}] {}'.format(response['id'], response['name']))