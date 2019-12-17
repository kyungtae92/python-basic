# 반환 여러개 (변수여러개, 리스트)

def circleProc(radius, height):
    cirArea = radius * radius * 3.14159265
    cirVol = cirArea * height

    return cirArea, cirVol      #리턴 값이 두 개 이상인 경우는 순서대로 리턴 받는다.

def main():
    radius = float(input('반지름 : '))
    height = float(input('원의 높이 : '))

    area, vol = circleProc(radius, height)

    print('반지름 %d인 원의 넓이 %.2f !' % (radius, area))
    print('반지름 %d인 원의 둘레 %.2f !' % (radius, vol))

main()