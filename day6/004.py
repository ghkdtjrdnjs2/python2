# f문자열
# replace : 치환
str4= "010-1111-2222"
# 함수 : 소속없는 함수 + 소속있는 메소드
print(len(str4))
# method : 특정 타입 소속 -> 타입은 함수도 가질 수 있다
# 문자열 메소드는 새로운 문자열을 만든다
str4.replace("-",".") #리플레이스 되지않고 그대로 나온다
print(str4)
# 문자열을 바꿀수 없기때문에 새로 하나를 더 만든다
# 문자열을 처리하는(다루는) 연산은 무조건 마지막에 대입(가르키다)해야한다
str4=str4.replace("-",".")
str4=str4.replace("1111","xxxx")
print(str4)

j1= "971011-2010015"
j1=j1.replace("010015","******") 
print(j1)

print(j1.replace(j1[8:],'******')) # 다른방법

str5="     aa aa     " # strip 공백 제거
print(str5.strip())
