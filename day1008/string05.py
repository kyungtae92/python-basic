# 문자열 입력받아서 반대로 출력

inStr = ""
outStr = ""
count = 0; i = 0

inStr = input("문자열을 입력하시오: ")
count = len(inStr)
print(count)

for i in range(0, count):
    outStr += inStr[count - (i + 1)]

print("문자열을 반대로 출력: %s" % outStr)
