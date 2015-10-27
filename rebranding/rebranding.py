#http://codeforces.com/problemset/problem/591/B
x,y = map(int, input().split())
input_str = input()
for _ in range(y):
    char1, char2 = map(str, input().split())
    input_str = input_str.replace(char1, '_')
    input_str = input_str.replace(char2, char1)
    input_str = input_str.replace('_', char2)

print(input_str)
