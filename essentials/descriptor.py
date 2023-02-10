#!/usr/bin/env python

# Python descriptor
# https://docs.python.org/3/howto/descriptor.html
"""
Descriptors are used throughout the language. It is how functions turn into bound methods. Common tools like classmethod(), staticmethod(), property(), and functools.cached_property() are all implemented as descriptors.

...

Defines descriptors, summarizes the protocol, and shows how descriptors are called. Provides an example showing how object relational mappings work.
Learning about descriptors not only provides access to a larger toolset, it creates a deeper understanding of how Python works.
"""


class EvenNumber:
    def __set_name__(self, owner, name):
        print(f"This attribute name is: {name}")
        # self.name = name

    def __get__(self, obj: object, type=None) -> object:
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        if value == 1:
            raise AttributeError

        obj.__dict__[self.name] = (value if value % 2 == 0 else 0)


class Values:
    value1 = EvenNumber()
    value2 = EvenNumber()
    value3 = EvenNumber()
    value4 = EvenNumber()

    def __str__(self) -> str:
        return f"Values{{{self.value1, self.value2, self.value3, self.value4}}}"


# my_values = Values()
# my_values.value1 = 3
# my_values.value2 = 4
# my_values.value3 = 20

# print(f"Totally: {my_values}")
