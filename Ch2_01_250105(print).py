# Ch2_01_ex1
# 파이썬 완전 기초
# Print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

#파이썬 3가지 print formatting + 자주 나오는 질문까지

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자

"""

### 3가지 Format Practices

x = 50
y = 100
text = 308276567
n = 'Cha'

# 출력1 %
ex1 = ' n = %s, s = %s, sum = %d' % (n, text, (x + y))
print(ex1)

# 출력2 format 함수
ex2 = ' n = {n}, s = {s}, sum = {sum}'.format(n=n, s=text, sum=x+y)
print(ex2)

# 출력3 f 스트링 
ex3 = f'n = {n}, s = {text}, sum={x+y}'
print(ex3)

# 구분기호
# 1000단위 별로 표시 
m = 100000000

print(f'm : {m:,}')
print(f'{m:,}') #이렇게 해도 값은 위와 값은 동일하게 나옴

print()

# 정렬
# ^ : 가운데 정렬, < : 왼쪽 정렬, > : 오른쪽 정렬

t = 20

print(f"t : {t:10}") # 10자리를 확보, 10칸 확보
print(f"t center : {t:^10}")
print(f"t center : {t:<10}")
print(f"t center : {t:>10}")

print()
print()

print(f"t center : {t:-^10}")
print(f"t center : {t:*^10}")
print(f"t center : {t:#^10}")
print(f"t center : {t:#<10}")
print(f"t center : {t:#>10}")

