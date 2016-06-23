
import copy
import munch

def dotify(obj):
    o = copy.deepcopy(obj)
    return munch.munchify(o)


class A:
    sa = {
            'name': 'class A, sa'
            }

    def foo(self):
        print('A, foo')
        print('A, sa: ', self.sa)
        print('A, sa: ', A.sa)


if __name__ == "__main__":
    print('yes, --main--')

    o = dict(
            a = 1,
            b = 2,
            c = range(3),
            d = 'what a akward dict'.split()
            )

    mo = dotify(o)

    a = A()
