import re

line = "pet:cat i love cats"
#  match = re.match(pattern,strint, <flag=0>)
print("match function ")
print(line)
match = re.match(r"pet:\w\w\w",line) # \w --> matches the any single character or digit or _
print(match)
print(match.group(0))
print("---------------------------")

match = re.search(r"pet:\w\w\w", line)
print("search function")
print(line)
print(match)
print(match.group(0))
print("---------------------------")

# what is difference match() and search()

print("search  function")
line = "i love cats pet:cat"
print(line)
match = re.search(r"pet:\w\w\w",line)   #    \w --> matches the any single character or digit or _
print(match)
print(match.group(0))
print("---------------------------")

print("match function")
print(line)
line = "i love cats pet:cat"
match = re.match(r"pet:\w\w\w",line)     # \w --> matches the any single character or digit or _
print(match)
#print(match.group(0))
print("---------------------------")

