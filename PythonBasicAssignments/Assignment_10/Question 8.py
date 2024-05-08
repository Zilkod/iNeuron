#8(a)
try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero!")
except ValueError:
    print("Error: Please enter valid numeric values!")

#8(b)
try:
    string = input("Enter a number: ")
    number = int(string)
    print("Converted integer:", number)
except ValueError:
    print("Error: Invalid input! Please enter a valid integer.")

#8(c)
try:
    my_list = [1, 2, 3, 4, 5]
    index = int(input("Enter the index to access: "))
    value = my_list[index]
    print("Value at index", index, ":", value)
except IndexError:
    print("Error: Index out of range! Please enter a valid index.")
except ValueError:
    print("Error: Invalid input! Please enter a valid integer index.")

#8(d)
try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero!")

#8(e)
try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    result = num1 / num2
    print("Result:", result)
except Exception as e:
    print("Error:", e)