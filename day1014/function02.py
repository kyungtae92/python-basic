def findMax(a, b, c):
    if a > b:
        bignumber = a
    else:
        bignumber = b

    if bignumber < c:
        bignumber = c
    return  bignumber

def main():
    bignumber = 0
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    bignumber = findMax(a, b, c)
    print("The biggest number : ", bignumber)

main()