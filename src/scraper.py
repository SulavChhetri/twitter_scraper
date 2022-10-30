from pathlib import Path
import os,json,csv
import requests

ROOT_DIR = Path(__file__).parent.parent
file_path = os.path.join(ROOT_DIR,'files')

# cookies = {
#     'guest_id_marketing': 'v1%3A166714578590594575',
#     'guest_id_ads': 'v1%3A166714578590594575',
#     'gt': '1586750557632356352',
#     '_sl': '1',
#     'kdt': 'PvlQYx0k3PF3Cxu38eHOHSeeDkzHrhBVrVCT2zO9',
#     'att': '1-aYbVSwMms50WviNvvTGOvUE1rWsW8dGx2MaC34ce',
#     'dnt': '1',
#     'personalization_id': '"v1_YHS4X2UiXdS97SD/uuxyRg=="',
#     'guest_id': 'v1%3A166714734246014126',
#     'ct0': 'b9ad0b5ce9c229cdadfe74e02469165c',
# }

headers = {
    'authority': 'twitter.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.6',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'guest_id_marketing=v1%3A166714578590594575; guest_id_ads=v1%3A166714578590594575; gt=1586750557632356352; _sl=1; kdt=PvlQYx0k3PF3Cxu38eHOHSeeDkzHrhBVrVCT2zO9; att=1-aYbVSwMms50WviNvvTGOvUE1rWsW8dGx2MaC34ce; dnt=1; personalization_id="v1_YHS4X2UiXdS97SD/uuxyRg=="; guest_id=v1%3A166714734246014126; ct0=b9ad0b5ce9c229cdadfe74e02469165c',
    'referer': 'https://twitter.com/Xulav58',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-csrf-token': 'b9ad0b5ce9c229cdadfe74e02469165c',
    'x-guest-token': '1586750557632356352',
    'x-twitter-active-user': 'yes',
    'x-twitter-client-language': 'en',
}

params = {
    'variables': '{"screen_name":"xulav58","withSafetyModeUserFields":true,"withSuperFollowsUserFields":true}',
    'features': '{"verified_phone_label_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true}',
}

def main():
    response = requests.get('https://twitter.com/i/api/graphql/HThKoC4xtXHcuMIok4O0HA/UserByScreenName', params=params,headers=headers).text
    jsonresponse = json.loads(response)
    data = jsonresponse['data']['user']['result']['legacy']
    birth_date_dict = jsonresponse['data']['user']['result']['legacy_extended_profile']['birthdate']
    birthdate = str(birth_date_dict['year'])+'-'+str(birth_date_dict['month'])+'-'+str(birth_date_dict['day'])
    user_name = data['screen_name']
    name =data['name']
    location = data['location']
    with open(os.path.join(file_path,'profile_data.csv'),'a') as file:
        writer = csv.writer(file)
        if file.tell()==0:
            writer.writerow(["Name","Username","Location","Date of Birth"])
        writer.writerow([name,user_name,location,birthdate])


main()