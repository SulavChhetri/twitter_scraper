from genericpath import isfile
from pathlib import Path
import os
import json
import csv
import requests

ROOT_DIR = Path(__file__).parent.parent
file_path = os.path.join(ROOT_DIR, 'files')


def guest_token_update():
    response = requests.post('https://api.twitter.com/1.1/guest/activate.json', headers={
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    }).text
    with open(os.path.join(file_path,'tokennumber.txt'), 'w',encoding='utf-8') as file:
        file.write(json.loads(response)['guest_token']) 

def param_variable(username):
    params = {
        'variables': {"screen_name":username,"withSafetyModeUserFields":True,"withSuperFollowsUserFields":True},
        'features': '{"verified_phone_label_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true}',
    }
    params['variables'] = json.dumps(params['variables'])
    return params

def extract_data(guest_token_number,username):
    headers = {
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'x-csrf-token': '42ad35cb76f583318cf67ccf0adae6bb',
        'x-guest-token': guest_token_number,
    }
    try:
        response = requests.get('https://twitter.com/i/api/graphql/HThKoC4xtXHcuMIok4O0HA/UserByScreenName', params=param_variable(username),headers=headers).text
        jsonresponse = json.loads(response)
        data = jsonresponse['data']
        if 'user' not in data.keys():
            return None
        return data['user']['result']['legacy']
    except:
        guest_token_update()
        guest_token_number = read_token_number()
        scrape_and_insert(guest_token_number,username)

def scrape_and_insert(guest_token_number,username):
    main_dict = extract_data(guest_token_number,username)
    if main_dict:
        scrape_into_csv(main_dict)
   

def scrape_into_csv(mainlist):
    with open(os.path.join(file_path,'profile_data.json'),'a',encoding="utf-8") as file:
        json.dump(mainlist,file)

def read_token_number():
    if os.path.isfile(os.path.join(file_path,'tokennumber.txt')):
        with open(os.path.join(file_path,'tokennumber.txt'), 'r',encoding='utf-8') as file:
            return file.read()
    else:
        return ''
        
def main(username):
    guest_token_number = read_token_number()
    scrape_and_insert(guest_token_number,username)


# main('xulav12345')