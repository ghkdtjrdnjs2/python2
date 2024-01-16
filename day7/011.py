# 숫자 리스트 - 추가, 목록, 삭제, 종료

numbers=[]

def print_menu():
    print('1.추가, 2.목록, 3.삭제, 999.종료')

def input_select():
    return input('메뉴 입력:')

def add_value():
     value = int(input('값:'))
     numbers.append(value)

def list_numbers():
    for num in numbers:
        print(num, end=" ")
    print()

def delete_number():
    value = int(input('삭제:'))
    index = 0




while True:
    print_menu()
    select = input_select()
    if select=='1':
        add_value()
    elif select=='2':
        list_numbers()
    elif select=='3':
        delete_number()
    elif select=='999':
        break

        

