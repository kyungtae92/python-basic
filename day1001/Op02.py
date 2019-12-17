# 원의 넓이 ,원의 둘레
# 반지름 , 파이
# 원의 둘레 : 2 * 반지름 * 파이
# 원의 넓이 : 반지름 * 반지름 * 파이
radius = 5
PI = 3.14159265
circleV = 2 * radius * PI
circleA = radius * radius * PI
print("원의 둘레 : ", circleV)
print("원의 넓이 : %f" % circleA)
print("반지름 ", radius, "인 원의 넓이는 ", circleA, "이다.")
# print("반지름 {} 인 원의 넓이는 {}입니다".format(radius, circleA))
print("반지름 %d 인 원의 둘레는 %.2f 이다." % (radius, circleV))
