# Put this at the top of your kata00.py file
kata = (19,42,21)
#print lenght and elements of the tuple kata: 
print("the {} numbers are:".format(len(kata)), ", ".join(str(i) for i in kata))