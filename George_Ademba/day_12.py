def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

number = 70
result = factorial_recursive(number)
print(f"The factorial of {number} is {result}")
