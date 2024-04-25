import math

def math_operations(x):
    logarithm = math.log(x)
    exponential = math.exp(x)
    power_of_2 = 2 ** x
    square_root = math.sqrt(x)
    return logarithm, exponential, power_of_2, square_root

number = int(input("Enter a number: "))
result = math_operations(number)
print("Logarithm:", result[0])
print("Exponential:", result[1])
print("Power of 2:", result[2])
print("Square Root:", result[3])
