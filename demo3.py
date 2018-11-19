import re

str = "we need to inform him with the latest information"

res = re.finditer('inform',str)
print(type(res))    #   <class 'callable_iterator'>
for i in res:
    locup = i.span()
    print(locup)
print(type(locup))  #  <class 'tuple'>

for i in re.finditer('info',str):
    locup = i.span()

    print(locup)