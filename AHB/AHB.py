#http://codeforces.com/problemset/gymProblem/100796/A
a,b = list(map(str, input().split()))
temp = []
for index in range(len(a)):
    ta = list(a)
    tb = list(b)
    t = int(ta[index]) - int(tb[index])
    temp.append(str(abs(t)))
print(int(''.join(temp)))