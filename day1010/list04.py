aa = []
for i in range(0, 4):
    aa.append(0)
sum = 0

for i in range(0, 4):
    aa[i] = int(input(str(i) + '번째 숫자: '))

sum = aa[0] + aa[1] + aa[2] + aa[3]
# for j in range(0, len(aa)):             # for문도 사용가능
#     sum = sum + aa[j]

# for j in aa:                            # 이렇게도 가능
#     sum = sum + j
print('총합: ', sum)
