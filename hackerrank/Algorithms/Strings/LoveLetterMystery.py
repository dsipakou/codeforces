n = int(input())
for i in range(n):
    output = 0
    s = input()
    for j in range(len(s) // 2):
        output += abs(ord(s[j]) - ord(s[-(j + 1)]))
    print(output)