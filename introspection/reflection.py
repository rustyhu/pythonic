"Get useful information from live Python objects -- use inspect module"

import inspect


def func_a(p1, p2):
    """
    This is demo doc of A.   
    """
    pass


def func_b(p1, p2):
    """
    This is demo doc B.   
    """
    pass


if __name__ == "__main__":
    "Get the meta properties of function"
    func_list = [func_a, func_b]
    func_map = {1: func_a, 2: func_b}

    title = """Welcome to this menu:\n"""
    line_text = "{}: {}"
    print(title)

    for (i, func) in enumerate(func_list):
        print(line_text.format(i+1, func.__doc__.strip()))

        sgnt = inspect.signature(func_a)
        # print(sgnt.bind(1, 2).args)
        print(sgnt)
