class MyClass:
    def my_method(self, x):
        return x * 2


def horder_fn(method, arg):
    return method(arg)


obj = MyClass()
result = horder_fn(obj.my_method, 5)
print(result)  # Output: 10


def horder_fn2(method, obj, arg):
    "Used to call class.method directly"
    return method(obj, arg)


# To use horder_fn() invoke TypeError:
# MyClass.my_method() missing 1 required positional argument: 'x'
print(horder_fn2(MyClass.my_method, obj, 5))
