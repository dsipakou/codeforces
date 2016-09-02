n = float(input())
tax = int(input())
toll = int(input())
print('The total meal cost is ' + str(round((tax/100 * n) + (toll/100 * n) + n)) + ' dollars.')
