x = int(input("출력할 별 수 입력>> "))

for i in range(1, x+1):
    for j in range(i):
        print("*", end='')
    print()


x = int(input("출력할 별 수 입력>> "))    # 거꾸로 출력
for i in range(1, x+1):
    for j in range(x+1-i):
        print("*", end='')
    print()

x = int(input("출력할 별 수 입력>> "))
for i in range(1, x+1):
    for j in range(x-i):
        print(' ', end= '')

    for k in range(i):
        print("*", end='')
    print()

x = int(input("출력할 별 수 입력>> "))    # 삼각형 출력
for i in range(1, x+1):
    for j in range(x+1-i):
        print(' ', end='')

    for k in range(2*i-1):
        print("*", end='')
    print()