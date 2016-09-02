import re
s = input()
s = re.sub(r'a?o?y?e?u?i?', '', s.lower())
print(''.join('.' + x for x in s))
