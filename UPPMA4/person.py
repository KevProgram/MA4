""" Python interface to the C++ Person class """
from numba import njit
import ctypes
from time import perf_counter as pc

# lib = ctypes.cdll.LoadLibrary('./libperson.so')

# class Person(object):
# 	def __init__(self, age):
# 		lib.Person_new.argtypes = [ctypes.c_int]
# 		lib.Person_new.restype = ctypes.c_void_p
# 		lib.Person_get.argtypes = [ctypes.c_void_p]
# 		lib.Person_get.restype = ctypes.c_int
# 		lib.Person_set.argtypes = [ctypes.c_void_p,ctypes.c_int]
# 		lib.Person_delete.argtypes = [ctypes.c_void_p]
# 		self.obj = lib.Person_new(age)

# 	def get(self):
# 		return lib.Person_get(self.obj)

# 	def set(self, age):
# 		lib.Person_set(self.obj, age)
        
# 	def __del__(self):
# 		return lib.Person_delete(self.obj)
_age= 10


def fib_py(n):
	if n <= 1:
		return n
	else:
		return (fib_py(n-1) + fib_py(n-2))


@njit
def fib_numba(n):
	if n <=1:
		return n
	else:
		return (fib_numba(n-1) + fib_numba(n-2))

f=Person(n)
f.fib()

start=pc()
print(fib_py(_age))
end=pc()
print("fib_py:", end-start)
start=pc()
print(fib_numba(_age))
end=pc()
print("numba: ", end-start)
print(fib(10))


# n= Person(_age)





	