n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    while a[i]%2==0: a[i]//=2
    while a[i]%3==0: a[i]//=3
print("YES" if max(a)==min(a) else "NO")