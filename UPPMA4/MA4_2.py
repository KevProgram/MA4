#!/usr/bin/env python3.9
from numba import njit
from time import perf_counter as pc
from person import Person
import matplotlib.pyplot as plot

def main():
	
	#Test

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
	
	N=9
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
	r= range(30, 45)
	for n in r:
		print('N: ', n)
		start = pc()
		fib_py(n)
		end = pc()
		fib_py_list.append(end-start)
		print('fib_py: ', end-start)

		start = pc()
		fib_numba(n)
		end = pc()
		fib_numba_list.append(end - start)
		print('fib_numba: ', end-start)

		start = pc()
		f = Person(n)
		f.fib()
		end = pc()
		fib_cpp_list.append(end - start)
		print('fibc: ', end-start)

	plot.plot(r, fib_py_list, label='Python')
	plot.plot(r, fib_numba_list, label='Numba')
	plot.plot(r, fib_cpp_list, label='C++')
	plot.savefig('plot_MA42.png')

#xaxs


	
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
