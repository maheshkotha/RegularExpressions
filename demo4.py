import re

str = "Sat, hat, mat, pat"

allstr = re.findall("[shmp]at",str)
for i in allstr:
    print(i)

print("--------------------")

allstr = re.findall("[Shmp]at",str)
for i in allstr:
    print(i)

print("--------------------")

allstr = re.findall("[h-p]at",str)
for i in allstr:
    print(i)

print("--------------------")

allstr = re.findall("[^h-m]at",str)
for i in allstr:
    print(i)

print("--------------------")