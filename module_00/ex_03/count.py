"""
• If None or nothing is provided, the user is prompted to provide a string.
• If the argument is not a string, print an error message.
• This function must have a docstring explaning its behavior.
Test your function with the python console
"""
import sys
import	string
def text_analyzer(str = None):
	"""
	This function counts the number of upper characters, 
	lower characters, punctuation and spaces in a given text.
	"""
	if (str == None):
		str = input("what is the text to analyze?\n")
	if (str.isdigit()):
		print("Error: the argument is not a string")
		quit()
	if (str == ""):
		print("No text to analyze")
		quit()
	up = 0
	low = 0
	punc = 0
	sp = 0
	for i in str:
		if i in string.punctuation:
			punc += 1
		elif i.isupper():
			up += 1
		elif i.islower():
			low += 1
		elif i.isspace():
			sp += 1
	print("""The text contains {} character(s):
- {} upper letter(s)
- {} lower letter(s)
- {} punctuation mark(s)
- {} space(s)""".format(len(str), up, low, punc, sp))

#so we can lunch count.py as a standalone program too
if __name__ == "__main__":
	l = len(sys.argv) - 1
	if l <= 1:
		if (l == 0):
			text_analyzer()
		else:
			text_analyzer(sys.argv[1])
	else:
		print("Error: invalid number of arguments\n")
