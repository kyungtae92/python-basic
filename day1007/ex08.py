import calendar

birth_year = int(input("당신이 태어난 년도를 입력하시오: "))
birth_month = int(input("몇 월에 태어났습니까? "))

print("\n아래는 당신이 태어난 달의 달력입니다.")
calendar.prmonth(birth_year, birth_month)