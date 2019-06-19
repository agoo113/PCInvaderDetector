import requests


def get_system_status():
    try:
        # Add your server url here
        url = 'server_url'
        response = requests.get(url + '/get_status')
        enabled = response.json()
        return enabled

    except:
        return False

