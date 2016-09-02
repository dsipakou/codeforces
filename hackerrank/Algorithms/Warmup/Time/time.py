import re

s = input()
numbers = re.findall('\d+', s)
frmt = re.findall('[A-Z]+', s)
if frmt[0] == 'AM':
    if numbers[0] == '12':
        numbers[0] = '00'
elif numbers[0] != '12':
    numbers[0] = str(int(numbers[0]) + 12)
print(':'.join(x for x in numbers))