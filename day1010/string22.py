# 입력한 문자 또는 문자열을 다른 문자열과 비교
# 현재 문자열에서 특정 문자 찾기?

str = input("문자열 입력>> ")

if str != "yes":
    print("yes 문자열 아님")
else:
    print("yes 문자열임")

a = [1,2,3,4,5,6,7]
if 7 not in a:
    print("7이 없음")
else:
    print("7이 있음")
    