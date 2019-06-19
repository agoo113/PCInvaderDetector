import requests

url = 'http://invader-detector.azurewebsites.net'
response = requests.get(url + '/get_status')
print(response.json())