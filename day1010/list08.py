
aa = [10,20,30]
aa[1] = 200     # 1번지 값 수정
print(aa)

bb = [10,20,30]
bb[1:2] = [200,201]     # 범위지정
print(bb)

cc = [10,20,30]
cc[1] = [200,201]       #값지정
print(cc)

dd = [10,20,30]
del(dd[1])
print(dd)
