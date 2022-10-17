import requests
import json

url = "https://superheroapi.com/api/your_token/search/"
heroes_list = ['Hulk', 'Captain America', 'Thanos']

def smart_hero(url, params):
    iq_dict = {}
    for hero in params:
        hero_dict = json.loads(requests.get(url + hero).content)
        iq_dict[hero] = int(hero_dict['results'][0]['powerstats']['intelligence'])
    return max(iq_dict, key=iq_dict.get)

print(smart_hero(url, heroes_list))