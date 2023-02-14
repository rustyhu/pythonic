# fly scratch

from typing import Any, Callable


class myproperty:
    "mock stdlib property"

    def __init__(
        self,
        fget=None,
        fset=None,
        fdel=None,
        doc=None,
    ):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.doc = doc

    def getter(self, __fget: Callable[[Any], Any]):
        self.fget = __fget
        return self

    def setter(self, __fset: Callable[[Any, Any], None]):
        self.fset = __fset
        return self

    def deleter(self, __fdel: Callable[[Any], None]):
        self.fdel = __fdel
        return self

    def __get__(self, __obj: Any, __type):
        if self.fget is None:
            raise AttributeError
        return self.fget(__obj)

    def __set__(self, __obj: Any, __value: Any) -> None:
        if self.fset is None:
            raise AttributeError
        self.fset(__obj, __value)

    def __delete__(self, __obj: Any) -> None:
        if self.fdel is None:
            raise AttributeError
        self.fdel(__obj)


class SimpleData:
    def __init__(self, ival) -> None:
        self._x = ival

    @myproperty
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        self._x = val

    # @x.deleter
    # def x(self):
    #     del self._x


if __name__ == '__main__':
    sd = SimpleData(30)
    print(sd.x)
    sd.x = 9
    print(sd.x)
    del sd.x
    # print(sd.x)