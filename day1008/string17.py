# def dateConvert(date):
#     temp = date.split('/')
#     newdate = str(temp[0] + '년')
#     newdate += str(temp[1] + '월')
#     newdate += str(temp[2] + '일')
#     return newdate
#
# def main():
#     indate = input('날짜 년월일 입력: ')
#     newdate = dateConvert(indate)
#     print(newdate)
#
# main()



code = input('주민번호 앞자리 6자리: ')

year = '19' + code[0:2]
month = code[2:4]
day = code[4:6]

age = 2019-int(year) + 1
print("당신은", year, "년에 태어났군요.")
print("당신의 생일은", month, "월", day, "일이 군요.")
print("당신의 올해", age, "살이군요.")