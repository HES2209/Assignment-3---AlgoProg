num1 = int(input("Enter your first numbers : "))
num2 = int(input("Enter your second numbers : "))

print("What do you want do calculate addition(+), minus(-), multiply(*),or divide(:) ")
symbols = input("Enter the symbols : ")

if symbols == '+' :
    result = num1 + num2
    print(result)
elif symbols == '-' : 
    result = num1 - num2
    print(result)
elif symbols == '*' :
    result = num1 * num2
    print(result)
elif symbols == ':' : 
    result = num1 / num2
    print(result)
else:
    print(f"{symbols} is not a valid")


