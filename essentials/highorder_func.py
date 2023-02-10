"ONLY A DEMO TO SHOW! Chain of high-order functions"


def assigna(a):
    def foo(a, b, c, d, e, f):
        return a + b + c + d + e + f

    return lambda b: lambda c: lambda d: lambda e: lambda f: foo(
        a, b, c, d, e, f)


# This is equivelant to an OO style struct - a class...


class Assigna:
    def __init__(self, a):
        self.a = a

    def ag_b(self, b):
        self.b = b
        return self

    def ag_c(self, c):
        self.c = c
        return self

    def ag_d(self, d):
        self.d = d
        return self

    def ag_e(self, e):
        self.e = e
        return self

    def ag_f(self, f):
        self.f = f
        return self

    def exe(self):
        return self.a + self.b + self.c + self.d + self.e + self.f


if __name__ == '__main__':
    ag_b = assigna(1)
    ag_c = ag_b(20)
    ag_d = ag_c(300)
    ag_e = ag_d(4000)
    ag_f = ag_e(50000)

    print(ag_f(600000))

    print(
        Assigna(1).ag_b(20).ag_c(300).ag_d(4000).ag_e(50000).ag_f(
            600000).exe())
