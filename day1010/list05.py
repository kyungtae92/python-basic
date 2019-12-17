aa = []
bb = []
value = 0

for i in range(0, 100):                     #정방향초기화
    aa.append(value)
    value += 2 # value = value + 2
print(aa)

for i in range(0, 100):                     #역방향초기화
    bb.append(aa[99-i])
print(bb)
