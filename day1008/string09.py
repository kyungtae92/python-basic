ss = input('아무거나 문자열을 입력하시오: ')
print("출력할 문자열 ==> ", end='')

if ss.startswith('(') == False:
    print("(", end='')

print(ss, end='')

if ss.endswith(')') == False:
    print(")", end='')
