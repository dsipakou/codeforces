s = list(input())
n = int(input()) - 1
output = 0
for i in range(len(s)):
    if s[i] == 'a':
        output += ((n - i) // len(s)) + 1
print(output)
