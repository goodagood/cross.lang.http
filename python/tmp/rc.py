
import json
import doctest

import requests

Address = "http://localhost:5565/json_input"


def json_input(addr = Address, the_json = {'ask4': 'ping'}):
    '''
    '''

    r = requests.post(addr, json = the_json)
    print(r.json())
    return r


def form_input():
    '''
    '''
    addr = 'http://localhost:9000/form_input'

    sample_dict = dict( a=1, b=2,
            sa = 'str a',
            sb = 'str b',
            )

    data = dict(
            some = 'some ....',
            json_in_text = json.dumps(sample_dict)
            )

    r = requests.post(addr, data)
    print(r.json())
    return r



rj = ijson()
