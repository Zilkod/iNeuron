height = int(input("Enter number of row: "))
for i in range(height):
    for j in range(height - i - 1):
        print(" ", end="")

    for k in range(2 * i + 1):
        print("*", end="")

    print()
