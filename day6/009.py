# 메뉴로 숫자를 입력받아 처리하는 프로그램 작성
# 1. 숫자 추가 2. 숫자 출력 3. 합계 4. 값으로 삭제 999. 종료
# print, input, int, 값을 확인하는 : in if~elif while True: break


num=[]
while True:
    print('===========================메뉴선택================================')
    select=input("1.숫자 추가, 2. 숫자 출력, 3. 합계, 4. 값으로 삭제, 999.종료")
    if select=='1':
     nums=int(input("숫자 추가:"))
     num.append(nums)
    elif select=='2':
      for num in nums:
       print(num)
    elif select=='3':
      print(f'합계:{sum(num)}')
    elif select=='4':
      val=int(input('값 삭제:'))
      if val in num:
        num.remove(val)
    elif select=='999':
      print("종료")
      break

