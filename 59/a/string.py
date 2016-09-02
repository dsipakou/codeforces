import re

s = input()
if len(re.findall('[A-Z]', s)) > len(re.findall('[a-z]', s)):
    print(s.upper())
else:
    print(s.lower())
