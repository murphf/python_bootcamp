# Put this at the top of your kata03.py file
kata = "The right format"
l = len(kata)
i = 0
k = 0
tire = 42 - l
while i < 42:
    if i < tire:
        print("-", end="")
        i += 1
    else:
        print(kata[k], end="")
        k +=1
        i += 1