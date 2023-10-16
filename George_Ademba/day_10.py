import calculator
x=int(input("First number: "))
y=int(input("Second number: "))
numbers=(x,y)
added=calculator.add(numbers)
subtracted=calculator.subtract(numbers)
multiplied=calculator.multiply(numbers)
divided=calculator.division(numbers)
print(f"When added, {added}, subtracted {subtracted}, multiplied {multiplied}, and when divided {divided}")