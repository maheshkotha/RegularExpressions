import re

str = "we need to inform him with the latest information"
res = re.search('inform',str)
print(type(res))
print(res)
if re.search('inform',str):
    print("Ther is here")

allinform = re.findall('inform',str)

print(type(allinform))
print(allinform)

for i in allinform:
    print(i)
