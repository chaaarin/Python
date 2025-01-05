# #ch_03_파이썬 숫자형
# 파이썬 숫자형 사용법
# 파이썬 모든 자료형
# 데이터 타입 선언
# 연산자 활용
# 형 변환
# 외부 모듈 사용

# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린 (true, false)
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
이 외에도 많은 자료형들이 있지만 우선 위 자료형은 기본적으로 알고 있어야함!
#시퀀스는 반복을 처리할 수 있고 어떤 순서가 있다는 것을 의미, 한줄로 줄 서있음!
"""

# 데이터 타입
str1 = "Python"
bool = True
str2 = 'Anaconda'
float_v1 = 10.0 # 10 == 10.0 다름! 
int_v1 = 7
list = [str1, str2] #이런게 시퀀스, str1, str2를 담을 수 있음
dict = {
    "name": "Machine Learning", # name, version 앞에 있는 것들을 key라고 함! Machine Learning을 꺼내기 위한 name key
    "version": 2.0
}
tuple = (7, 8, 9)
set = {3, 5, 7}

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v1))
print(type(int_v1))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))

# 숫자형 연산자
"""
+
-
*
/ : 나누기
// : 나눈 후 몫만 계산
% : 나눈 후 나머지만 계산
abs(x) : 절대값
pow(x, y) : x의 y제곱을 계산함 = x ** y -> 2 ** 3 = 8 -> (pow(2, 3)) 이렇게 써도 동일
x ** y : 제곱
complex(x) : 복소수
"""

# 정수 출력
i = 77
i2 = -14
big_int = 7777777777779999999999999999 #자바에선 큰 수는 다르게 처리해야하는데 파이썬은 그냥 쓰면 된다! 내부적으로 이만큼의 공간 확보 후 값 넣을 수 있음

print(i)
print(i2)
print(big_int)
print()

# 실수 출력
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

print(f)
print(f2)
print(f3)
print(f4)
print()

# 연산 실습
i1 = 39
i2 = 939
big_int1 = 777777777777777999999999292323
big_int2 = 982376984327498273944332312
f1 = 1.234
f2 = 3.939

# + 더하기
print(">>>>>+더하기")
print("i1+i2 : ", i1 + i2)
print("f1+f2 : ", f1 + f2)
print("big_int1+big_int2 : ", big_int1 + big_int2)

a = 3 + 1.0
print(a) 
print(type(a), a) # 형변환이 자동으로 이루어짐
print()

# - 빼기
print(">>>>>-뺴기")
print("i1-i2 : ", i1 - i2)
print("f1-f2 : ", f1 - f2)
print("big_int1-big_int2 : ", big_int1 - big_int2)
print()

# * 곱하기
print(">>>>>*곱하기")
print("i1*i2 : ", i1 * i2)
print("f1*f2 : ", f1 * f2)
print("big_int1*big_int2 : ", big_int1 * big_int2)
print()

# / 나누기
print(">>>>>/나누기")
print("i1/i2 : ", i1 / i2)
print("f1/f2 : ", f1 / f2)
print("big_int1/big_int2 : ", big_int1 / big_int2)
print()

# // 몫 계산
print(">>>>>// 몫")
print("i1//i2 : ", i1 // i2)
print("f1//f2 : ", f1 // f2)
print("big_int1//big_int2 : ", big_int1 // big_int2)
print()

# % 나머지 계산
print(">>>>>%나머지")
print("i1 % i2 : ", i1 % i2)
print("f1 % f2 : ", f1 % f2)
print("big_int1 % big_int2 : ", big_int1 % big_int2)
print()

# ** 제곱 계산
print(">>>>>**제곱")
print("i1 ** i2 : ", i1 ** i2)
print("f1 ** f2 : ", f1 ** f2)
# print("big_int1 ** big_int2 : ", big_int1 ** big_int2) 너무 숫자가 왕왕큼
print()

# 형 변환 연습
a = 3. # 3.0 이랑 같음 0을 생략 할 수 있음
b = 6
c = .7
d = 12.7


# 타입 출력
print(type(a), type(b), type(c), type(d))

# 형 변환
print(float(b)) #6을 플롯으로 바꿈
print(int(c)) #소수자리 나오지 않고 0으로 형변환
print(int(d))
print(int(True)) # 숫자가 아닌데 1이 나옴!, True : 1, False : 0으로 나옴 1은 참 0은 거짓
print(float(False))
print(float(True))
print(complex(3)) #가수부와 허수부..? 실수부? 아무튼 정확히 복소수로 변환해서 나옴 / 복소수는 거의 쓸 일이 없음
print(complex('3')) #동일하게 문자열로 3을 넣어도 파이썬은 복소수는 숫자를 받아야 하지만 문자열을 넣어도 내부적으로 숫자형으로 바꾼 후 실행함! 똑똑이임
print(complex(False))
print()

# 수치 연산 함수
print(abs(-7)) #절대값을 돌려줌, 절대값이 7임
x, y = divmod(100, 8) # divmod 함수라는게 있음. 100을 8로 나눈 다음에 뭐가 나오는지 확인
print(x, y)
print(pow(5, 3), 5 ** 3) #제곱 5를 3번 곱함

print()

# 외부 모듈
import math #수학 계산을 도와주는 패키지

#ceil 함수
print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수 -> 5.1이상의 가장 작은 정수는 6!

#floor

#pi 원주율이 나옴
print(math.pi)

