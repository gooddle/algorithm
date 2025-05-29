
# 세 정수의 최댓값 구하기 함수형
def max3(a, b, c):
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum

print(max3(1, 2, 4)) # 4
print(max3(1, 2, 3)) # 3

# 중앙 값 구하기
def med3(a, b, c):
    if a >= b:
        if b>=c:
            return b
        elif a<= b:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b


med = med3(1, 2, 3)
print(med)

## 오름 차순 후 중간 값 선정 (리스트 이용)
def sorted_med3(a, b, c):
    return sorted([a, b, c])[1]

print(sorted_med3(1, 2, 3)) ## 2

# 조건문 분기
n = int(input('정수를 입력하세요.:'))

if n % 2 == 0:
    print("짝수입니다.")
elif n % 2 == 1 and n > 0:
    print("홀수입니다.")
elif n < 0:
    print("음수입니다.")
elif n == 0:
    print("0입니다.")
else:
    pass

## 조건 연산자 삼항 연산자
x = int(input("정수를 입력하세요"))
y = int(input("정수를 입력하세요"))
a = x if x > y else y
print(a)