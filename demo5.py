import re

str = "hat rat mat pat"

res = re.compile('[r]at')

print(res)          #  re.compile('[r]at')
print(type(res))    #  <class '_sre.SRE_Pattern'>

alt = res.sub("alter",str)
print(alt)

