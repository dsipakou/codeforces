# http://codeforces.com/problemset/problem/574/A
n = int(input())
a = list(map(int, input().split()))
main = a[0]
rest = sorted(a[1:], reverse=True)
counter = 0
while True:
    rest = sorted(rest, reverse=True)
    if main > rest[0]:
        print(counter)
        exit()
    else:
        main += 1
        rest[0] -= 1
        counter += 1

