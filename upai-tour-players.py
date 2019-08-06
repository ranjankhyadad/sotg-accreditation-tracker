#!/usr/bin/python3

import requests
import json
import os

# Obtain this from https://upai.usetopscore.com/u/oauth-key
CLIENT_ID = os.getenv('UPAI_CLIENT_ID')
CLIENT_SECRET = os.getenv('UPAI_CLIENT_SECRET') 
BASE_URL = 'https://upai.usetopscore.com'
assert CLIENT_ID, 'Need to set UPAI_CLIENT_ID envvar'
assert CLIENT_SECRET, 'Need to set UPAI_CLIENT_SECRET envvar'

data = {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,

}

response = requests.post('{}oauth/server'.format(BASE_URL), data=data)
ACCESS_TOKEN= response.json()['access_token']
header = {'Authorization': 'Bearer {}'.format(ACCESS_TOKEN)}

def get_tournaments(year=None, header=None):
    url = '{}{}?&per_page=100&order_by=date_desc'.format(
        BASE_URL, '/api/events'
    )
    r = requests.get(url, headers=header)
    tournaments = r.json()['result']
    if year is not None:
        tournaments = [
            t for t in tournaments if t['start'].startswith(str(year))
        ]
    return tournaments

def get_registrations(event_id=None, header=None):
    url = '{}{}?&id={}'.format(
        BASE_URL, '/api/registrations', '113044'
    )
    r = requests.get(url, headers=header)
    registrations = r.json()['result']
    print(r.json()['status'])
    return registrations


if __name__ == '__main__':
    year = 2012
    #tour_events = get_tournaments(None,header) 
    registrations = get_registrations(None, header)
    print(registrations)
