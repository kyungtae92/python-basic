# IF 4가지 형식
# 단독 if , if~else, if~elif~elif...else, 중첩if(if문 안에 if)

num = int(input("정수입력: "))

if num > 100:                                           # if
    print("100보다 크다")


if num > 100:                                           # if~else
    print("100보다 크다")
else:
    print("100보다 작다")


# A와 B가 같고, B와 C가 같으면 A와 C가 같다                # 중첩 if
a = 10; b = 10; c = 20
if a == b:
    if b == c:
        if a == c:
            print("A와 C는 같다.")
    else:
        print("A와 C는 같지 않다.")
else:
    print("A와 C는 같지 않다.")
