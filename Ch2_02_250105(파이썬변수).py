#ch_02_파이썬 변수
#다양한 변수 선언법
# - 변수 할당 설명
# - Object Identity
# - 변수 네이밍 규칙
# - 예약어

# 변수란? 프로그램에 있어서 어떤 숫자나 문자등을 저장하는 공간

# 기본 선언
n = 700

# 출력
print(n)
print(type(n)) #type은 n이라는 변수에 할당되어있는 값에 자료형을 보여줌, 출력하면 n에 있는 700은 int 로 보여줄거임 = 정수!라는 말
print(n * 700)
print()

# 동시 선언
x = y = z = 700
print(x, y, z)
print()

# 선언 > 내가 선언한 변수를 잘 알고있기, 의도하지 않은 값들이 출력되거나 계산될 수 있음 = 오류!!
var = 75
# 재선언 
var = "Change Value"
print(var)
print(type(var))
# 출력 시 아래와 같은 값으로 출력됨. 즉, 기존에 선언된 75라는 값은 참조, 가져올 수 없음! 덮어써버림 마지막 선언값으로 재할당 되기 때문에,,
# Change Value
# <class 'str'>

# Object References 
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
#3. 콘솔 출력

# ex1)
print(300)
print(int(300)) # 내부적으로 이러한 것들이 일어남

# ex2)
# n = 777
n = 777 #파이썬이 내부적으로 판단
print(n, type(n))
print()

m = n # 777을 m에다가 복사! n을 치환하면 777
# m -> 777 <- n
print(m, n)
print(type(m), type(n))
print()

m = 400
print(m, n)
print(type(m), type(n))
print()

# 중요중요 id(identity)확인 : 객체의 고유값 확인

m = 800
n = 655

print(id(m)) # 800이라는 정수를 id 값을 기준으로 이렇게 가져옴...!?
print(id(n))
print()
#출력하면 두 값이 다름!
print(id(m) == id(n)) # false 로 나옴
print()

m = 800
n = 800
z = 800
i = 800 # 이렇게 4개의 똑같은 값을 가진 변수는 똑같은 하나의 인스턴스라고 볼 수 있음, 보기에는 4개를 선언했으나 1개만 존재함! = 인터프리터, 파이썬 엔진

print(id(m)) 
print(id(n))
print()
print(id(m) == id(n)) # True 로 나옴
samenum = (m, n, z, i)
print(samenum)
print()

m = 800
n = 800 * 2 # 이렇게 달라질때만 다른 인터페이스를 만들어냄
print(id(m)) 
print(id(n))
print()

# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -> Method를 주로 선언할 때 사용
# Pascal Case : NumberOfColleageGraduates -> Class를 주로 선언할 때 사용 , 굳이 변수에 선언하지는 않음
# Snake Case(파이썬에서 많이 사용) : number_of_colleage_graduates  -> 파이썬에서 변수 선언 시 많이 사용

students_grade = 3
print(students_grade)

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8
#특수문자 또는 숫자로 시작하는 변수는 에러남 _, $만 허용함

print(age, Age,aGe, AGE, a_g_e, _age, age_, _AGE_)
print()

# 예약어는 변수명으로 불가능 -> 이미 파이썬에서 사용하는 언어들
#for = 3
#print(for) # 에러남

# python reserved words 검색하면 확인 가능 , List of Keywords in Python

# 아래 예약어들은 변수명으로 불가능
"""
False
def
id
raise
None
del
import
return
True
elif
in
try
and
else
is
while
as
except
lambda
with
assert
finally
nonlocal
yield
break
for
not
class
from
or
continue
global
pass
"""



