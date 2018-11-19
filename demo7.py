import re

str = '12345 123 12345 12355 1234567 12321356 mah3sh'

print("Matches",len(re.findall("\d{5,7}",str)))


num = '623-432-4567'

if re.search("[6-9]{1}\d{2}-\d{3}-\d{4}",num):
    print("it is phone number")