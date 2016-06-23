import json

da = dict(a=1, b=2, c='cc')

sda = json.dumps(da)

bda = json.loads(sda)
