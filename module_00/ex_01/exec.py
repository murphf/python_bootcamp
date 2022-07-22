"""
program that takes a string as argument,
reverses it, swaps its letters case
and print the result.
"""

import sys
l = len(sys.argv)
s = ""
if (l > 1):
	for i in range (1, l):
		s +=  sys.argv[i] 
		if i != (l - 1):
			s += ' '
	s = s.swapcase()[:: -1]
	print (s)