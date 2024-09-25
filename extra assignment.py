n = int(input("Input a number that wanted to be factoralized : "))
def factor(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factor(n - 1)
print(f"The factorial of {n} is {factor(n)}.")

