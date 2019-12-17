# 리스트는 중복되는 값이 들어감
# listID = []
#
# listID.append(2001)
# listID.append(2001)
# listID.append(2001)
# listID.append(2001)
# for i in listID:
#     print(i, end=' ')



listID = []

listID.append(2001)
listID.append(2002)
listID.append(2003)
listID.append(2004)


for m in listID:
    if listID.index(m) == 2:    # 두번째 인덱스
        print("%d %s" % (listID.index(m), m))

for m in listID:
    if listID.index(m) == 2:    # 두번째 인덱스
        listID[2] = 'DDD'
print(listID)