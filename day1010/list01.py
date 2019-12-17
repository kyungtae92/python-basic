# LIST 사용법

# 1.리스트 초기화
aa = [0,0,0,0,0,0,0]
bb = [1,2,3,4,5,6,7,8,9,10]
cc = [] # 최초 생성 리스트 초기화

aaSize = len(aa)
print(aaSize)

bbSize = len(bb)
print(bbSize)

ccSize = len(cc)
print(ccSize)

str = []
for i in range(0,1000):
    str.append(0)
    print(str[i], end='')
print()
str1 = []
for i in range(0,1000):
    str1.append(i)
    print(str1[i], end='')

