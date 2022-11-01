import requests,json,os,csv
from pathlib import Path
ROOT_DIR = Path(__file__).parent.parent
file_path = os.path.join(ROOT_DIR, 'files')

def guest_token():
    response = requests.post('https://api.twitter.com/1.1/guest/activate.json', headers={
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    }).text
    return json.loads(response)['guest_token']

params = {
        'variables': '{"screen_name":"chiddyafc","withSafetyModeUserFields":true,"withSuperFollowsUserFields":true}',
        'features': '{"verified_phone_label_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true}',
    }

def main():
    headers = {
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'x-csrf-token': '42ad35cb76f583318cf67ccf0adae6bb',
        'x-guest-token': guest_token(),
    }
    response = requests.get('https://twitter.com/i/api/graphql/HThKoC4xtXHcuMIok4O0HA/UserByScreenName', params=params,headers=headers).text
    jsonresponse = json.loads(response)
    data = jsonresponse['data']['user']['result']['legacy']
    try:
        birth_date_dict = jsonresponse['data']['user']['result']['legacy_extended_profile']['birthdate']
        birthdate = str(birth_date_dict['year'])+'-'+str(birth_date_dict['month'])+'-'+str(birth_date_dict['day'])
        print(birthdate)
    except Exception as e:
        print(e)
    user_name = data['screen_name']
    name =data['name']
    location = data['location']

    # with open(os.path.join(file_path,'profile_data.csv'),'a',encoding="utf-8") as file:
    #     writer = csv.writer(file)
    #     if file.tell()==0:
    #         writer.writerow(["Name","Username","Location","Date of Birth"])
    #     writer.writerow([name,user_name,location])

main()