class MyMeta(type):

    counter = 0

    def __init__(cls, name, bases, dic):
        # print("My name is", name)
        type.__init__(cls, name, bases, dic)
        cls._order = MyMeta.counter
        MyMeta.counter += 1


class MyTypeA(metaclass=MyMeta):
    pass


class MyTypeB(metaclass=MyMeta):
    pass


class MyTypeC(metaclass=MyMeta):
    pass


if __name__ == "__main__":
    print(f"Count class: {MyMeta.counter}")

    print(f"""Get _order from:
    MyTypeA: {MyTypeA._order}
    MyTypeB: {MyTypeB._order}
    MyTypeC: {MyTypeC._order}
""")
