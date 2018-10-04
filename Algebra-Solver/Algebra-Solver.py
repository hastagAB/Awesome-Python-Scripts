#!/usr/bin/python3

from sympy import *
import sys

def solver(x):
	sympy_eq = sympify("Eq(" + x.replace("=", ",") + ")")
	result = solve(sympy_eq)
	return result[0]

def main(x):
	X = solver(x)
	print("X = " + str(X))

if __name__ == "__main__":
	main(sys.argv[1])