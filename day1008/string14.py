# 문자열 입력받아서 그 중에 'o' -> '$' 로 변경

ss = input('문자열 입력: ')
print('출력 문자열-> ', end='')

for i in range(0, len(ss)):
    if ss[i] != 'o':
        print(ss[i], end='')
    else:
        print('$', end='')
