#!/usr/bin/env python3.9
from numba import njit
from time import perf_counter as pc
from person import Person

def main():
	
	

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
	
	N=10
	fib_py_list= []
	fib_numba_list=[]
	fib_cpp_list=[]

	f=Person(N)
	f.fib()
	def caller():
		for i in range [30:45]:
			fib_py_list(i).append
		return fib_py_list
	print(caller())



# _age= 10
# start=pc()
# print(fib_py(_age))
# end=pc()
# print("fib_py:", end-start)
# start=pc()
# print(fib_numba(_age))
# end=pc()
# print("numba: ", end-start)
	

	
# n= Person(_age)




if __name__ == '__main__':
	main()
