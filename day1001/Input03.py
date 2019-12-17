# 입력된 나이에 10년 후에 나이값 계산

name = input("당신의 이름은 무엇? ")
print("%s님 반갑습니다." % name)
# print("{}님 반갑습니다.".format(name))
age = input("How old are you? ") # 문자형 숫자...
print("10년 후에 당신의 나이는 %d세 입니다." % (int(age)+10))
# print("10년 후에 당신의 나이는 {}세 입니다.".format(int(age) + 10))