import os
from src.scraper import *


def filedeleter(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)

def file_data_checker(file_path):
    with open(file_path,'r') as file:
        content = file.read()
        if content != '':
            return True
        else:
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
    assert extract_data(guest_token_number,'xulav12345')==['Xulav', 'xulav12345', 'Nepal', '2000-9-9']

if __name__=="__main__":
    # test_guest_token_update()
    # test_param_variable()
    test_extract_data()