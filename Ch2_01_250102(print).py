# Ch2_01 
# 파이썬 완전 기초
# Print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

#print(인수=파라미터 넣어줘야함)

#기본 출력
print('Python Start!')
print("Python Start!")
print() #띄어쓰기 됨
print() #띄어쓰기 됨
print('''Python Start!''') # 3개 짜리는 프린트 문에서는 잘 사용하지 않음
print("""Python Start!""")

print() 

# seperator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep=' ') #원하는 옵션으로 출력하고 싶다면 sep = ' ' 사용 > 띄어쓰기되어 한 글자씩 노출 P Y T H O N
print('P', 'Y', 'T', 'H', 'O', 'N', sep='    ')
print('P', 'Y', 'T', 'H', 'O', 'N', sep=' , ')

print ('010', '7777', '1234', sep='-')

print('python', 'google.com', sep='@')
print()

#end 옵션
print('Welcome to', end='   ') #마지막 끝날 때 어떻게 할건지
print('IT News', end='  ')
print('Web Site')
print()

#file 옵션
import sys
print('Learn Python', file=sys.stdout) #learn python을 파일 옵션에 어떤 특정한 파일로 사용할거다를 뜻함
print()

#format 사용 ( digit = 정수열, string = 문자열, float = 실수(소수))
print('%s %s' % ('one', 'two'))
print('{} {}' .format('one', 'two'))
print('{1} {0}' .format('one', 'two'))
print()

# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))
print()
print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^0}'.format('nice')) #중앙정렬
print('%.5s'%('nice'))
print('%.5s'%('pythonstudy'))#.을 붙이면 절삭함! 슬라이싱함!
print('{:10.5}'.format('pythonstudy')) #공간은 10개가 있고 5개만 출력됨
print()

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))
print('%4d'%(42))
print('%4d'%(4245235))
print('{:4d}'.format(42))
print()

# %f
print('%f' % (3.1411212534))
print('%1.18f' % (3.1411212534)) # 1=정수부, . ~ 소수부
print('{:f}'.format(3.123235213412))
print('%06.2f'%(3.141592653589793))
print('{:06.2f}'.format(3.141592653589793))


