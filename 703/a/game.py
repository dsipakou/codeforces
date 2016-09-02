n = int(input())
sum = 0
for i in range(n):
    l = list(map(int, input().split()))
    if l[0] > l[1]:
        sum += 1
    elif l[0] < l[1]:
        sum -= 1
if sum > 0:
    print('Mishka')
elif sum < 0:
    print('Chris')
else:
    print('Friendship is magic!^^')
