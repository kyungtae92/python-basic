# 윤년을 판단하는 문제해결
# 4나누어 떨어지고, 100으로 나누어 떨어지지 않음.
# 400으로 나누어 떨어짐.
# 방법1
import calendar
year = int(input("윤년을 확인할 년도 입력(2019): "))

if year % 400 == 0:
    print(year, "년은 윤년입니다.")
    calendar.prmonth(year, 2)
elif year % 100 == 0:
    print(year, "년은 윤년이 아닙니다.")
    calendar.prmonth(year, 2)
elif year % 4 == 0:
    print(year, "년은 윤년입니다.")
    calendar.prmonth(year, 2)
else:
    print(year, "년은 윤년이 아닙니다.")
    calendar.prmonth(year, 2)

# 방법2
import calendar
year = int(input("윤년을 확인할 년도 입력(2019): "))

if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
    print(year, "년은 윤년입니다.")
    calendar.prmonth(year, 2)
else:
    print(year, "년은 윤년이 아닙니다.")
    calendar.prmonth(year, 2)
