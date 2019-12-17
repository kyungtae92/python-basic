# 원의 넓이 : 반지름 * 반지름 * 3.14
# 원의 둘레 : 원의 넓이 * 높이

def circleArea(radius):
    print('radius: ', id(radius))
    area = radius * radius * 3.14
    return area

def circleVolume(radius, height):
    vol = circleArea(radius) * height
    return  vol

def printCircle(area, vol, radius):
    print('반지름 %d인 원의 넓이 %.2f !' % (radius, area))
    print('반지름 %d인 원의 둘레 %.2f !' % (radius, vol))

def main():
    radius = int(input('반지름 : '))
    height = int(input('원의 높이 : '))
    area = circleArea(radius)
    vol = circleVolume(radius, height)
    printCircle(area, vol ,radius)
    print('radius: ', id(radius))
main()
