"This show it is quite cumbersome to communicate in C++ datatypes using stdlib ctypes."

from ctypes import CDLL, c_bool

cpp_mod = CDLL("./libtmpcpp.so")

pgeek = cpp_mod.Wrap_new()
gmf = cpp_mod.Wrap_myFunction
gmf.restype = c_bool

for i in range(1, 10):
    print(gmf(pgeek, i))

cpp_mod.Wrap_show(pgeek)