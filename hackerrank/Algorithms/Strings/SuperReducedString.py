s = list(input())
output = list()
index = 1
while (index < len(s)) and (len(s) > 1):
    for i in range(index, len(s)):
        if s[i] == s[i - 1]:
            del s[i]
            del s[i - 1]
            index = 1
            break
        else:
            index += 1
print((''.join(x for x in s) if len(s) > 0 else 'Empty String'))