#!/usr/bin/env python3.9
from numba import njit
from time import perf_counter as pc
from person import Person
import matplotlib.pyplot as plt

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
	
	
	fib_py_list= []
	fib_numba_list=[]
	fib_cpp_list= []
	
	fib_numba_list_2=[]
	fib_py_list_2=[]
	
	r=range(30,36)
	l=range(20,31)
	
#Question 5: py and numba for n=20-30
	for n in l:
		print('N: ', n)
		start = pc()
		fib_py(n)
		end = pc()
		fib_py_list_2.append(end-start)
		print('fib_py: ', end-start)

		start = pc()
		fib_numba(n)
		end = pc()
		fib_numba_list_2.append(end - start)
		print('fib_numba: ', end-start)
#Question 4: all for n=30-45
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


	plt.plot(r, fib_py_list, label='Python')
	plt.plot(r, fib_numba_list, label='Numba')
	plt.plot(r, fib_cpp_list, label='C++')
	plt.savefig('plot_MA42.png')
#Question 6: Calculate n=47 with numba and C++
	n_6=40

	#C++
	start=pc()
	f=Person(n_6)
	f.fib()
	end=pc()
	print('C++ n=47: ',end-start)

	#Numba
	start=pc()
	fib_numba(n_6)
	end=pc()
	Q6_numba.append(end-start)
	print('Numba n=47: ', Q6_numba)

	







if __name__ == '__main__':
	main()
