import requests


def get_system_status():
    try:
        # Add your server url here
        url = 'http://51.140.164.169'
        response = requests.get(url + '/get_status')
        enabled = response.json()
        return enabled

    except:
        return False
