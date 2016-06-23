
from pprint import pprint


oo = {
        'one': 1,
        'two': 2,
        'nest': {
            'sub1': 1.1,
            'sub2': 1.2
            },

        'str1': 'I am a string'
        }

'''
room8 = dd.street.building.layer8.green.room[8]


'''

class Dots:
    def __init__(self, data):
        if type(data) is not dict:
            raise Exception('for dict only')

        self.private_data = data
        self.private = []


    def __getattr__(self, name):
        self.private.append(name)
        return self

    def end(self):
        print('in end')
        current = self.private_data

        for name in self.private:
            if name in current:
                current = self.private_data[name]
            else:
                current[name] = {}
                current = current[name]

        #if current == None:
        #    raise Exception('what else should it be?')

        return current





def point_to(data):
    pass


if __name__ == "__main__":

    doo = Dots(oo)
    #doo.aa.bb.end()
    d = doo.aa.bb.cc.end()
    print(type(d))
    d = 'new assignment'
    print(d)
    pprint(doo.private)
    #d = 'some thing'
    pprint(oo)

    #_ = 11
    #print('_ :', _)
    #print('_ + 11 :', _ + 11)
