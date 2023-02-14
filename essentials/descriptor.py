#!/usr/bin/env python
"""
Any object which defines the methods __get__(), __set__(), or __delete__(). When a class attribute is a descriptor, its special binding behavior is triggered upon attribute lookup. Normally, using a.b to get, set or delete an attribute looks up the object named b in the class dictionary for a, but if b is a descriptor, the respective descriptor method gets called. Understanding descriptors is a key to a deep understanding of Python because they are the basis for many features including functions, methods, properties, class methods, static methods, and reference to super classes.

...
Descriptors are used throughout the language. It is how functions turn into bound methods. Common tools like classmethod(), staticmethod(), property(), and functools.cached_property() are all implemented as descriptors.

...
Defines descriptors, summarizes the protocol, and shows how descriptors are called. Provides an example showing how object relational mappings work.
Learning about descriptors not only provides access to a larger toolset, it creates a deeper understanding of how Python works.

...
The following methods only apply when an instance of the class containing the method (a so-called descriptor class) appears in an owner class (the descriptor must be in either the owner’s class dictionary or in the class dictionary for one of its parents). 
"""

# https://docs.python.org/3/glossary.html#term-descriptor
# https://docs.python.org/3/howto/descriptor.html#descriptor-protocol
# https://docs.python.org/3/reference/datamodel.html#descriptors


class EvenNumber:
    def __set_name__(self, owner: type, name):
        print(f"Class is {owner}, this attribute name is: {name}")
        self.attribute_name = name

    def __get__(self, obj: object, owner=None) -> object:
        return obj.__dict__.get(self.attribute_name, 0)

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.attribute_name] = (value if value % 2 == 0 else 0)


class Values:
    value1 = EvenNumber()
    value2 = EvenNumber()
    value3 = EvenNumber()
    value4 = EvenNumber()

    def __str__(self) -> str:
        return f"Values{{{self.value1, self.value2, self.value3, self.value4}}}"


my_values = Values()
my_values.value1 = 3
my_values.value2 = 4
my_values.value3 = 20
my_values.value4 = 1
print(f"Show: {my_values}")

two_val = Values()
print(f"Show: {two_val}")
