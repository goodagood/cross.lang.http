
import json
import importlib

from bottle import route, request, run

@route('/json_input', method='POST')
def json_input():
    j = request.json
    print("j: ", j)

    result = j['output'] = { 'the number': 46 }

    result = serve(j)

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
    return serve(jsonJob)





def serve(j):
    return {
            'retu.is.json.in.text': False,
            'haha':                 'you haha when you laugh' ,
            'input':                j,
            'output':               'some kind of no output'
            }


run(host='localhost', port=5565)
