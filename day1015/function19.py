# 여러개 매개변수



def para_func(*param):
    result = 0
    for num in param:
        result = result + num
    return result

def main():
    hap = para_func(10, 20)
    print("매개변수가 2개인 함수 호출 -> %d" % hap)

    hap = para_func(1,2,3,4,5,6,7,8,9,10)
    print("매개변수가 10개인 함수 호출 -> %d" % hap)

main()