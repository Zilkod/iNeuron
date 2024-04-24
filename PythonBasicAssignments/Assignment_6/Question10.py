length = int(input("Enter initial length: "))
spaces = 0
while length >= 1:
    print(" " * spaces, end="")
    print("|" * length)

    length -= 2
    spaces += 1
