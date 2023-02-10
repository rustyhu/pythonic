"getattr(), setattr(), dir() and so on"

import sys


class tmp:
    "short name to call from outside"

    def show(self):
        print(f"I am the {self.__class__} class!")


def str_to_class(classname: str, modname: str = __name__):
    try:
        return getattr(sys.modules[modname], classname)

    except BaseException as e:
        raise AttributeError('classname {} not found.'.format(classname))


cname = input("Input a class name you want to get a instance: ")
a = str_to_class(cname)()


print(f"This is {type(a)}, with attributes: {dir(a)}")
fname = input("Input function name you want to call: ")
getattr(a, fname)()
