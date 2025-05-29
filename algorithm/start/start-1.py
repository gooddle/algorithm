print("세 정수의 최댓값을 구합니다")
a = int(input("정수 a의 값을 입력하세요. :"))
b = int(input("정수 b의 값을 입력하세요. :"))
c = int(input("정수 c의 값을 입력하세요. :"))

maximum = a # 가장 큰 값을 a에 할당
if b > maximum: maximum = b # b가 maximum보다 크먼 최댓값은 b
if c > maximum: maximum = c # c기 maximum보다 크면 최댓값은 c

print(f"최대 값은 {maximum} 입니다.")

## 문자열 과 숫자 입력받기
print('이름을 입력하세요. :', end='')
name = input()
print(f'인녕하세요! {name}')

#문자열 정수로 변환
print(int('17')) ## 문자열 -> 정수

print(int('0b110',2)) ## 2진수 문자열 -> 10진수 정수 변환

print(int('0o75',8)) ## 8진수 문자열 -> 10진수 정수 변환

print(int('13',10)) ## 10진수 문자열 -> 10진수 정수 변환

print(int('0x3F', 16)) ## 16진수 문자열 -> 10진수 변환

print(float('3.14')) ## 문자열 실수형으로 변환