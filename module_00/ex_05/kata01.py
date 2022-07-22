# Put this at the top of your kata01.py file
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}
#k being a dictionary key and kata[k] its value
for k in kata:
	print("{} was created by {}".format(k, kata[k]))