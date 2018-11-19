import re

email = "m@.com ma@y.com @go.in email@mail.in"

print("Email Matches:", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}",email)))