s = list(input())
t = int(input())
output = 0
for i in range(1, len(s)):
    found = True
    if len(s) % i == 0:
        for j in range(i):
            if len(set(s[j::i])) > 1:
                found = False
        if found:
            print(t // i)
            exit()
print(t // len(s))
