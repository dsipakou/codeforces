h = int(input())
m = list(input())
m = [int(m[0]), int(m[1])]
minutes = ''
digits = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 11: 'eleven',
          12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'quarter', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
          19: 'nineteen', 10: 'ten', 20: 'twenty', 30: 'half', 40: 'fourty', 45: 'quarter', 50: 'fifty'}

if m == 0:
    print(digits[h], 'o\'clock', sep=' ')
else:
    if m[0] == 0:
        minutes = digits[m[1]]
