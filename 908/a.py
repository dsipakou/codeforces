s = input()
mask = ['a', 'e', 'i', 'o', 'u', '1', '3', '5', '7', '9']
output = 0
for i in range(len(s)):
    if s[i] in mask:
        output += 1
print(output)