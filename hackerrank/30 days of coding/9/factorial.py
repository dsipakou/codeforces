def factorial(n):
    if n > 1:
        return int(n) * int(factorial(n - 1))
    else:
        return 1
print(factorial(int(input())))
