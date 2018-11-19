import re

str = "hat rat mat pat"

res = re.compile('[r]at')

print(res)          #  output is ---> re.compile('[r]at')
print(type(res))    #  output is ---> <class '_sre.SRE_Pattern'>

alt = res.sub("alter",str)
print(alt)

