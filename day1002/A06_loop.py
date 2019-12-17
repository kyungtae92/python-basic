# 팩토리얼 5! = 120 => 5*4*3*2*1

fac = 1
x = int(input('팩토리얼 구할 수: '))

for i in range(x, 0, -1):
    fac = fac * i

print(fac)

fac = 1
x = int(input('팩토리얼 구할 수: '))

for i in range(x, 0, -1):
    if i != 1:
        print("%d * " % (i), end='')
    elif i == 1:
        print("%d = " % (i), end='')
        
    fac = fac * i

print(fac)