# 구구단 loop

dan = 2

while dan <= 9:
    print("===", dan, "단 ===")
    i = 1

    while ( i <= 9 ):
        print(dan, "*", i, "=", dan*i)
        i = i + 1

    dan = dan + 1
print("-------------------------------")

dan = 2
while dan <= 9:
    print("===", dan, "단 ===")
    for i in range(1, 10):
        print(dan, "*", i, "=", dan * i)
    dan = dan + i
print("-------------------------------")

dan = 2
for dan in range(2, 10):
    print("===", dan, "단 ===")
    for i in range(1, 10):
        print(dan, "*", i, "=", dan * i)
print("-------------------------------")

for i in range(1, 10):
    for j in range(2, 10):
        print("%d*%d=%2d " % (j, i, j*i), end= ' ')
    print("\n")
    