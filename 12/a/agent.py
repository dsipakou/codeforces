n = list()
for x in range(3):
    n.append(input())
if n[0] == n[2][::-1] and n[1][0] == n[1][2]:
    print("YES")
else:
    print("NO")