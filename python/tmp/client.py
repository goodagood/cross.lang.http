
import json
#import doctest

import requests

Address = "http://localhost:5565/json_input"


def json_input(addr = Address, the_json = {'ask4': 'ping'}):
    '''
    '''

    r = requests.post(addr, json = the_json)
    print(r.json())
    return r


def form_input(addr = Address, data = {'ask4': 'ping'}):
    '''

    The form would be:
        <input type="text" name="json_in_text">
    '''

    form_data = dict(json_in_text = json.dumps(data))

    r = requests.post(addr, data = form_data)
    print(r.json())
    return r



