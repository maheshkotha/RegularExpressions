import re

randstr = "her is \\drogba"

print(re.search(r'\\drogba',randstr))

rstr = '''
keep the blue flag
flying high
chesea
'''
print(rstr)
reg = re.compile("\n")
rstr = reg.sub(" ",rstr)
print(rstr)
print(rstr)
reg = re.compile("f")
rstr = reg.sub("\b",rstr)
print(rstr)
reg = re.compile("e")
rstr = reg.sub("\f",rstr)
print(rstr)
reg = re.compile("\f")
rstr = reg.sub("\v",rstr)
print(rstr)
reg = re.compile("\v ")
rstr = reg.sub("\t",rstr)
print(rstr)