## while 문 (반복문)

print("1부터 n까지의 정수 합을 구합니다.")
n = int(input("n:"))

sum1 = 0
i = 1

while i <= n:
    sum1 += i
    i += 1

print(f"정수의 합은 {sum1}")



## for 문
## 마지막 인데스는 포함 하지않음
##  ranage 범위 설정 ranage(a,b,step) step 간격으로
sum2 = 0
for i in range(1, n + 1): ## 마지막 인데스는 포함 하지않음 ranage 범위 설정 ranage(a,b,step) step 간격으로
    sum2 += i

print(f"정수의 합은 {sum2}")

## 오름 차순 정렬

print('a 부터 b 까지 정수의 합 계산')
a = int(input("정수를 입력하세요:"))
b = int(input("정수를 입력하세요 :"))

if a > b :
    a,b = b,a ## 스왑 a 가 b보다 크면 a 랑 b 값 바꿈

sum3 = 0
for i in range(a, b + 1):
    sum3 += i

print(f'{a}부터 {b} 사이 원소 합은 {sum3} ')

## 요소 합 과정 나타내기
## c와 d가 같으면 c = d 출력
## 1~5 라면 1+2+3+4+5 = 15
print('c 부터 d 까지 정수의 합 계산')
c = int(input("정수를 입력하세요:"))
d = int(input("정수를 입력하세요 :"))
if c > d:
    c,d = d,c
sum4 = 0
for i in range(c, d + 1):
    if i < d:
        print(f'{i} + ', end = '')
    else:
        print(f'{i} = ', end = '')
    sum4 += i

print(sum4)

## 개선 for문 안에 if문 제거
print('f 부터 e 까지 정수의 합 계산')
f = int(input("정수를 입력하세요:"))
e = int(input("정수를 입력하세요 :"))

if f > e:
    f,e = e,f
sum5 = 0
for i in range(f,e):
    print(f'{i} + ', end = '')
    sum5 += i

print(f'{e} = ', end = '')
sum5 += e
print(sum5)