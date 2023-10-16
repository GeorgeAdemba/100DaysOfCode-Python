number_one=int(input("Number one: "))
number_two=int(input("Number two: "))
try:
    divide=number_one/number_two
    print(f"{number_one} divided by {number_two} is {divide}")
except ZeroDivisionError:
    print("Can't divide by zero")