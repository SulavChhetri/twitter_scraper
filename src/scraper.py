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
    response = requests.get('https://twitter.com/i/api/graphql/HThKoC4xtXHcuMIok4O0HA/UserByScreenName', params=param_variable(username),headers=headers).text
    jsonresponse = json.loads(response)
    data = jsonresponse['data']['user']['result']['legacy']
    user_name = data['screen_name']
    name =data['name']
    location = data['location']
    try:
        birth_date_dict = jsonresponse['data']['user']['result']['legacy_extended_profile']['birthdate']
        birthdate = str(birth_date_dict['year'])+'-'+str(birth_date_dict['month'])+'-'+str(birth_date_dict['day'])
    except:
        birthdate = None
    return [name,user_name,None if location=='' else location,birthdate]

def scrape_and_insert(guest_token_number,username):
    mainlist = extract_data(guest_token_number,username)
    if mainlist:
        scrape_into_csv(mainlist)
   

def scrape_into_csv(mainlist):
     with open(os.path.join(file_path,'profile_data.csv'),'a',encoding="utf-8") as file:
        writer = csv.writer(file)
        if file.tell()==0:
            writer.writerow(["Name","Username","Location","Date of Birth"])
        writer.writerow(mainlist)

def read_token_number():
    with open(os.path.join(file_path,'tokennumber.txt'), 'r',encoding='utf-8') as file:
        return file.read()

def main(username):
    guest_token_number = read_token_number()
    try:
        scrape_and_insert(guest_token_number,username)
    except:
        print("not there")
        guest_token_update()
        guest_token_number = read_token_number()
        scrape_and_insert(guest_token_number,username)


# main('xulav12345')