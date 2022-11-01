import os
from src.scraper import *


def filedeleter(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)

def file_data_checker(file_path):
    try:
        with open(file_path,'r') as file:
            content = file.read()
            if content != '':
                return True
            else:
                return False
    except:
        return False

def test_guest_token_update():
    token_file_path = os.path.join(file_path,'tokennumber.txt')
    filedeleter(token_file_path)
    guest_token_update()
    assert os.path.isfile(token_file_path) == True
    assert file_data_checker(token_file_path) == True

def test_param_variable():
    username='xulav12345'
    param_data = param_variable(username)
    assert type(param_data)==dict
    assert type(param_data['variables'])==str
    assert (username in param_data['variables'])== True

def test_extract_data():
    guest_token_number = read_token_number()
    assert type(extract_data(guest_token_number,'xulav12345'))==dict
    assert extract_data(guest_token_number,'xulav12345')['name']=='Xulav'
    assert extract_data(guest_token_number,'chiddyafc')['screen_name']=='chiddyafc'

def test_scrape_and_insert():
    guest_token_number = read_token_number()
    json_file_path = os.path.join(file_path,'profile_data.json')
    filedeleter(json_file_path)
    scrape_and_insert(guest_token_number,'xulav12345')
    assert file_data_checker(json_file_path)== True

def test_scrape_into_csv():
    json_file_path = os.path.join(file_path,'profile_data.json')
    filedeleter(json_file_path)

    guest_token_number = read_token_number()
    mainlist = extract_data(guest_token_number,'xulav12345')
    scrape_into_csv(mainlist)
    assert file_data_checker(json_file_path)== True

# def test_read_token_number():


def test_main():
    json_file_path = os.path.join(file_path,'profile_data.json')
    token_file_path = os.path.join(file_path,'tokennumber.txt')
    filedeleter(token_file_path)
    filedeleter(json_file_path)
    main('xulav12345')
    assert file_data_checker(token_file_path) == True
    assert file_data_checker(json_file_path) == True

if __name__=="__main__":
    # test_guest_token_update()
    # test_param_variable()
    # test_extract_data()
    # test_scrape_and_insert()
    # test_scrape_into_csv()
    test_main()