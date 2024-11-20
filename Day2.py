#문자열의 첫번째=0번째 글자 가져오기
#Subscripting
print("Hello"[4])

#String
print("123" + "345") #+ 기호를 이용하면 더하는게 아닌 문자열을 더해줌

#Integer = Whole number
print(123 + 345)

#Large integers ex) 10,000 여기서 ,처럼 사용하는걸 _이걸로 사용함
print(123_456_789)
print(123456789)

#Float = Floating Point Number
print(3.12345)

#Boolean
print(True)
print(False)

#len 함수는 정수와 함께 작동하는 것을 좋아하지 않음
print(len("12345"))

#데이터 타입 알 수 있음
print(type("Hello"))

print(int("123") + int("456"))

int()
float()
str()
bool()

name_of_the_user = input("Enter your name ")
len_of_name = len(name_of_the_user)
print("Number of letters in your name : " + str(len_of_name))