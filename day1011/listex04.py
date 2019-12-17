# 리스트 원소에서 특정 값 찾기
# => 인덱스 번호로 나옴

heros = ['스파이더맨', '헐크', ' 캡틴마블', '아이언맨', '앤트맨', '토르']

if '헐크' in heros:
    print(heros.index('헐크'))
    print('헐크는 힘이 쎄다.')

index = heros.index('토르')   # 리스트에서 값이 있는지 찾고 있으면 번호를 알려준다
print(index)
