i = int(input())
big = i // 7 * 2 + min(2, i % 7)
small = i // 7 * 2 + max(0, i % 7 - 5)
print(small, big)