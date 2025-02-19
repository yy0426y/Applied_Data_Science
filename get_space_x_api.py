import requests
import json


def get_spacex_launches():
    api_url = 'https://api.spacexdata.com/v4/launches'
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None


launches = get_spacex_launches()
if launches:
    for launch in launches:
        print(f"Mission Name: {launch.get('name')}, Launch Date: {launch.get('date_utc')}")