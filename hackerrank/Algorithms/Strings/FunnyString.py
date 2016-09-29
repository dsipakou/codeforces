n = int(input())
for i in range(n):
    output = 'Funny'
    s = input()
    si = s[::-1]
    for j in range(1, len(s)):
        if abs(ord(s[j]) - ord(s[j - 1])) != abs(ord(si[j]) - ord(si[j - 1])):
            output = 'Not Funny'
            break
    print(output)