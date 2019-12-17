class Bird:
    birdName = ""
    birdSize = 0

    def __init__(self, birdName, birdSize):
        self.birdName = birdName
        self.birdSize = birdSize

    def __del__(self): #소멸자(생성자의 반대 개념), 객체가 메모리에서 해제될때 수행되는 코드
        print('객체가 메모리에서 해제됨 (소멸)')

    def ptrBird(self):
        print("Bird Name: ", self.birdName)
        print("Bird Size: ", self.birdSize)

class Eagle(Bird):  #Eagle 클래스가 Bird 클래스를 상속받은 형태
    def scanEagle(self):
        print("독수리가 눈으로 스캔한다!!!")

    def ptrBird(self):  #Bird 클래스의 ptrBird함수를 Eagle클래스에서 오버라이딩(코드 재정의)
        print("Eagle Name: ", self.birdName)
        print("Eagle Size: ", self.birdSize)

if __name__ == '__main__':
    # bird1 = Bird('수리부엉이', 500)
    # bird1.ptrBird()
    eagle1 = Eagle('독수리', 1000)
    eagle1.ptrBird()

    del(eagle1)