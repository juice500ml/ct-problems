s = input("Input string : ")
l = []
for c in s:
    if c in "aeiouAEIOU":
        l.append(c)

print(l,len(l))
