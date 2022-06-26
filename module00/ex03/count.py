import	string
def text_analyzer(str = None):
	"""
	function takes a string and displays:
	the sums of its upper-case characters,
	lower-case characters, punctuation characters and spaces.
	"""
	if (str == None):
		str = str(input("gives us a string"))
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

text_analyzer()
#print(text_analyzer.__doc__)