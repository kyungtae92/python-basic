# 2차원 리스트 행렬

list2 = []      #행 담당
list1 = []      #열 담당
value = 1

for i in range(0, 10):
    for j in range(0, 10):
        list1.append(value)
        value += 1
    list2.append(list1)     # 생성된 열 리스트를 행리스트에 추가
    list1 = []

sum = 0
for i in range(0, 10):
    for j in range(0, 10):
        print("[%3d] " % list2[i][j], end='')
        sum = sum + list2[i][j]
    print()
print("sum: ", sum)