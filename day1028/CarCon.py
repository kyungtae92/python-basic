# 클래스 사용이유는 API
class Car:
    color = ""  #클래스 내부의 변수(인스턴스 변수:필드:속성)
    speed = 0

    def __init__(self): #기본 생성자
        print('가장 먼저 수행되는 부분')
        print('클래스 내부 변수들을 초기화한다')
        self.color = "레드"
        self.speed = 120

    def __init__(self, color, speed):  #매개변수있는 생성자
        self.color = color
        self.speed = speed

    def ptrCar(self):   #클래스 내부의 함수
        print('차량의 색상은 ', self.color)
        print('차량의 속도는 ', self.speed)

    def getSpeed(self):
        return self.color

    def getColor(self):
        return self.speed

if __name__ == '__main__':
    mycar1 = Car('파란색', 200)
    mycar1.ptrCar()
    print('getSpeed() : ', mycar1.getSpeed())
    print('getColor() : ', mycar1.getColor())
