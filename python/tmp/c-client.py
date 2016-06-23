
# fail:?
#from . import client
#import .client
#from .client import *

import client

r = client.json_input()
print(r.text)
print(r.json())
