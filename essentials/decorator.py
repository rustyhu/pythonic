"Just a syntax suger, name substituting"

# You can do anyone callable to decorate another callable object:
# function deco function, class deco function, class deco classes...
# (classes are callable, as are instances of classes with a __call__() method.)


class Deco:
    "A simple class for decorating"

    def __init__(self, origf):
        self.f = origf

    def show(self):
        print("Powerful start!\n", self.f())


@Deco
def origf() -> str:
    return "original content"


# equivelant to
# origf = Deco(origf)
origf.show()


def ClassDeco(origCall):
    class Deco:
        "A decorating class"

        def __init__(self):
            self.c = origCall

        def show(self):
            print("Powerful start!\n", self.c())

    return Deco


@ClassDeco
class OrigC:
    def __init__(self) -> None:
        self.a = 30

    def __str__(self) -> str:
        return f"OrigC {{{self.a}}}"


# OrigC is ClassDeco.<locals>.Deco
OrigC().show()