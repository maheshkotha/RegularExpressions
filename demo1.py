import re

nameage = ''' Mahesh is 25 and Malli is 23,
              Satya is 22 and Satesh is 24'''

age = re.findall(r'\d{1,3}', nameage)
name = re.findall(r'[A-Z][a-z]*',nameage)

agedict = {}

x = 0
for eachname in name:
    agedict[eachname] = int(age[x])
    x +=1

print(agedict)