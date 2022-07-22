from ast import Return
import	sys
"""
a program that takes two integers A and B as arguments
and prints the result of the following operations:
Sum:	     A+B
Difference:  A-B
Product:     A*B
Quotient:    A/B
Remainder:   A%B
"""

#remove the decimal part if it's only 0
#e.g: 42 instead of 42.0
def	float_or_int(a):
	if (int(a) == a):
		return (int(a))
	return (a)

#take two floats: a and b and print the results of the 4 operations
def op(a, b):
	S = float_or_int(a + b)
	P = float_or_int(a * b)
	D = float_or_int(a - b)
	if (b != 0):
		Q = float_or_int(a / b)
		R = float_or_int(a % b)
	else:
		Q = "ERROR (division by zero)"
		R = "ERROR (modulo by zero)"
	print("""Sum:	     {}
Difference:  {}
Product:     {}
Quotient:    {}
Remainder:   {}""".format(S, D, P, Q, R))

#msg for our 3 possible errors
def	error(e = 0):
	if (e == 0):
		print("""Usage: python operations.py <number1> <number2>
	Example:
		python operations.py 10 30""")	
	elif (e == 1):
		print("AssertionError: invalid number of arguments")
	else:
		print("AssertionError: only integers")

if __name__ == "__main__":
	l = len(sys.argv)
	if (l == 1):
		error(0)
	elif (l > 3 or l < 3):
		error(1)
	else:
		a = sys.argv[1]
		b = sys.argv[2]
		if (not (a.isdigit() and b.isdigit())):
			error(2)
		else:
			op(float(a), float(b))