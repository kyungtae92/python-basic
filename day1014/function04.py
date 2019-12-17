def radiusInput():
    radius = float(input('반지름 입력>> '))
    return radius

def proceCircle(radius, PI):
    circleArea = radius * radius * PI
    return circleArea

def ptrCircle(radius, circleArea):
    print("반지름이 %.2f인 인 경우는 " % radius)
    print("원의 넓이가 %f 이다." % circleArea)

def main():
    # 변수 및 상수 선언부
    PI = 3.14159265

    # 입력부 -> radiusInput(), 매개변수 없음, 리턴값은 float 값으로 한 개 필요
    radius = radiusInput()   # r = float(input('반지름 입력>> '))

    # 처리부 -> proceCircle(), 매개변수 2개(반지름, 파이), 리턴값 float 값으로 한 개 필요
    circleArea = proceCircle(radius, PI)   # circleArea = r * r * PI

    # 출력부 -> ptrCircle(), 매개변수 2개, 리턴값 없음
    # print("반지름이 %.2f인 인 경우는 " % r)
    # print("원의 넓이가 %f 이다." % circleArea)
    ptrCircle(radius, circleArea)

main()
