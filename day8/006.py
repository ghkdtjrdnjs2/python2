# for 문
# hello를 for를 이용해 3번 출력하시오
#for x in (1,2,3):
#    print('hello')

#for x in range(3):
#    print(x)

# for을 이용해서 0~10 사이의 짝수
# if는 둘중의 셋중의.... for 반복
#for x in range(11):
#    if x%2==0:
#        print(x)

# 1부터 5의 합계를 출력 : 15
# for : 필요함
# if : 필요없음
# 파이썬 변수는 타입을 가진다 - 값에 따라 정해진다
# 숫자는 일단 걍 0 넣는다

result=0
for x in range(1,6):
    result=result+x

print(result)                 # 15