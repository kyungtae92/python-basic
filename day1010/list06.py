aa = [10,20,30,40]

print("aa[-1]는 %d, aa[-2]는 %d" % (aa[-1], aa[-2]))

bb = [10,20,30,40,50]

print(bb[0:3])  # 리스트에서 0번지부터 2번지까지 의미
print(bb[2:4])  # 리스트에서 2번지부터 3번지까지 의미
print(bb[2:])   # 리스트에서 2번지부터 끝까지 의미
print(bb[:2])   # 리스트에서 제일 앞번지부터 1번지까지 의미

# 리스트에는 + , *
cc = [10,20,30]
dd = [40,50,60]

print(cc + dd)  # 리스트 변수끼리 더하면 리스트가 합쳐진다
print(cc * 3)   # 리스트 변수에 어떤 숫자를 곱하면 해당 리스트가 숫자만큼 합쳐진다
