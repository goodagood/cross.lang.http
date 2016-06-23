
import json
import sys
import os
import importlib

from urllib.parse import urlparse

from bottle import route, request, run


@route('/json_input', method='POST')
def json_input():
    j = request.json
    print("/json_input get j: ", j)

    #result = j['output'] = { 'the number': 46 }

    result = find_output(j)

    return result


@route('/help')
def help():
    return '''
        <p>
            post job data as:
        </p>
        <p>
            curl --data "json_in_text=The_serialized_json_data"  host:port/ask4
        </p>
    '''


@route('/form_input', method='POST')
def form_input():
    json_in_text = request.forms.get('json_in_text')
    print("""json_in_text: %s"""%json_in_text)
    print(type(json_in_text))

    try:
        jsonJob = json.loads(json_in_text)
    except Exception as e:
        print('in except')
        print(e)
        return {'error': 'parse json_in_text error'}


    # job_name = j['ask4']
    # answer(j) gives a json: {
    #   ...
    #   'served.is.json.in.text': True/False,
    #   'served': {    # This should be the a json data
    #   }
    #   ...
    # }
    return find_output(jsonJob)



def set_path(task_path = '.'):
    absp = os.path.abspath(task_path)
    sys.path.append(absp)


def find_output(j):
    '''
    j: json input
    '''
    if 'ask4' not in j:
        j['pong'] = 'PONG'
        return j

    ask4 = j['ask4']

    try:
        print('to find module: ', ask4)
        mod  = importlib.import_module(ask4)
        output = mod.main(j)
        return dict(input=j, output=output)
    except Exception as e:
        return dict(input=j, error=str(e))


def start_server(url = None, host = 'localhost', port = 5565):
    if type(url) is str:
        # parse url
        o = urlparse(url)
        _host = o.hostname
        _port = o.port
        run(host=_host, port=_port)
        pass
    else:
        run(host=host, port=port)



if(__name__ == "__main__"):
    #run(host='localhost', port=5565)

    set_path('./tmp')
    start_server()

