# 021010-3410234
code = input("주민등록번호 13자리 전체 입력>>")

year = "20" + code[0:2]
month = int(code[2:4])
day = int(code[4:6])
gender = int(code[7:8])

age = 2019 - int(year) + 1
print("당신은", year,"년도에 태어났음")
print("당신의 생일은", month,"월 입니다")
print("당신의 올해", age,"세 입니다")

if gender == 3:
    print("당신은 남성입니다")
elif gender == 4:
    print("당신은 여성입니다")
    