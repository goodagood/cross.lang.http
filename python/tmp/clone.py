
a = dict(a=1, b=2)

b = dict(name='b', c=3, d=4)

def defaults(a, b):
    for k,v in b.items():
        a.setdefault(k,v)
