import json

import http.client, urllib.parse

address = 'localhost:9000/ask4'
Host = 'localhost'
Port = 9000

jtext = json.dumps(dict(
    a= 'aa',
    b= 'bb',
    one= 1,
    two= 2
    ))

print('jtext ', jtext)

params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue',
    '@action': 'show',
    'json_in_text': jtext})

#headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
headers = {"Content-type": "application/x-www-form-urlencoded"}

#conn = http.client.HTTPConnection("bugs.python.org")
conn = http.client.HTTPConnection(Host, Port)

#conn.request("POST", "", params, headers)
conn.request("POST", "/ask4", params, headers)
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
print("data ", data)
conn.close()



