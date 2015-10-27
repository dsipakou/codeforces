#http://codeforces.com/problemset/problem/590/A
from datetime import datetime
lenght = int(input())
nums = list(map(int, input().split()))
counter = 0
time = datetime.now()
for _ in range(lenght):
    tmp = []
    for index in range(len(nums)):
        if index == 0:
            tmp.append(nums[index])
        elif index == len(nums) - 1:
            tmp.append(nums[index])
            if tmp == nums:
                print(datetime.now() - time)
                print(counter)
                print(' '.join(str(e) for e in tmp))
                exit()
            else:
                counter += 1
                nums = tmp
        else:
            tmp_three = [nums[index - 1], nums[index], nums[index + 1]]
            tmp_three.sort()
            tmp.append(tmp_three[1])
print("-1")