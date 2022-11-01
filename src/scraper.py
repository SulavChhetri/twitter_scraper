from pathlib import Path
import os
import json
import csv
import requests

ROOT_DIR = Path(__file__).parent.parent
file_path = os.path.join(ROOT_DIR, 'files')

name_list = ['xulav12345', 'chiddyafc', 'Vishweshsoni', 'SujanLamsal100',
             'pratimakoiral12', 'nbasanta10222', '_SanChh_', 'GauravPoudel13', 'RomanPoudel12']


def guest_token():
    response = requests.post('https://api.twitter.com/1.1/guest/activate.json', headers={
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    }).text
    return json.loads(response)['guest_token']


def param_variable(username):
    params = {
        'variables': '{"screen_name":"xulav12345","withSafetyModeUserFields":true,"withSuperFollowsUserFields":true}',
        'features': '{"verified_phone_label_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true}',
    }

    username_variable = params['variables'].split('"')
    username_variable[3]=username
    params['variables'] = '"'.join(username_variable)
    # params_variable = json.loads(params['variables'])
    # params_variable['screen_name'] = username
    # params_variable = json.dumps(params_variable)
    # params['variables']= params_variable
    return params

def main(namelist):
    guest_token = guest_token()
    headers = {
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'x-csrf-token': '42ad35cb76f583318cf67ccf0adae6bb',
        'x-guest-token': guest_token,
    }
    for username in namelist:
        response = requests.get('https://twitter.com/i/api/graphql/HThKoC4xtXHcuMIok4O0HA/UserByScreenName', params=param_variable(username),headers=headers).text
        jsonresponse = json.loads(response)
        data = jsonresponse['data']['user']['result']['legacy']
        birth_date_dict = jsonresponse['data']['user']['result']['legacy_extended_profile']['birthdate']
        birthdate = str(birth_date_dict['year'])+'-'+str(birth_date_dict['month'])+'-'+str(birth_date_dict['day'])
        user_name = data['screen_name']
        name =data['name']
        location = data['location']
        with open(os.path.join(file_path,'profile_data.csv'),'a',encoding="utf-8") as file:
            writer = csv.writer(file)
            if file.tell()==0:
                writer.writerow(["Name","Username","Location","Date of Birth"])
            writer.writerow([name,user_name,location])


# main(name_list)
print(param_variable('chiddyafc'))