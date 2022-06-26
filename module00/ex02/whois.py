"""
program that takes a number as argument, 
checks whether it is odd, even or
zero, and print the result
"""
import sys
l = len(sys.argv)
if (l == 2):
	if (sys.argv[1].isdigit()):
		num = int(sys.argv[1])
		if (num == 0):
			print("I'm Zero")
		elif (num % 2):
			print("I'm Odd")
		else:
			print("I'm Even")
	else:
		print("AssertionError: argument is not an integer")
elif (l > 2):
	print("AssertionError: more than one argument are provided")
