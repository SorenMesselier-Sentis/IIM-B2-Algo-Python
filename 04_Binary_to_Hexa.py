def converter():
    binary_enter = input("Which binary code do you want to convert :\n ")
    decimal = int(binary_enter, 2)
    hexadecimal = hex(decimal)
    print(hexadecimal)
converter()