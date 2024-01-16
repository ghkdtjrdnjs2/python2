# 1에서 10까지의 합계 : 55
#result= 0
#for x in range(1,11):
#    result=result+x
#
#print(result)                  # 55
#
## 1에서 10까지의 3의 배수 출력
#d=0
#for x in range(1,11):
#    if x%3==0:
#        print(x)              # 3 6 9
#
#for x in range(1,11):
#    if x%3!=0:
#        continue           # 컨티뉴는 반복을 스킵
#    print(x)

# 1~10 사이의 3의 배수의 합계 -> 3 6 9 -> 18

#z=0
#for x in range(1,11):
#    if x%3==0:
#        z=z+x      
#print(z)

# 1~100사이의 5와 7의 공배수를 출력 35 70

#for x in range(1,101):
#    if x%5==0 and x%7==0:
#        print(x)

# 1~100 사이의 5의 배수와 7의 배수를 출력. 단 공배수는 제외 35랑 75빼고 출력
# 5 10 15 20 25 30 (35) 40 45 50 55 60 65 (70) 75 80 85 90 95 100
# 7 14 21 28 (35) 42 49 56 63 (70) 77 84 91 98 

for x in range(1,101):
    if x%5==0 and x%7==0:
        continue
    if x%5==0 or x%7==0:
        print(x, end=" ")


#for x in range(1,101):
#    if x%5==0 and x%7!=0:
#        print(x)
#    if x%5!=0 and x%7==0:
#        print(x)




        

