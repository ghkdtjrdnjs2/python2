# 할일 관리 만들기
# 할일번호, 할일, 성공여부

todos = []

todos.append({'tno':3, 'title':'학원 가기', 'finish':False})
todos.append({'tno':3, 'title':'학원 가기', 'finish':False})
todos.append({'tno':3, 'title':'학원 가기', 'finish':False})


def print_todos():
    for todo in todos:
        print(todo)

def add_todo():
    pass

def change_todo():
    pass

def delete_todo():
    pass

while True:
    print('할일 관리')
    print('1:목록, 2:할일추가, 3:할일 변경, 4:할일 삭제, 999: 종료')
    select = input('번호입력:')
    
    if select=='1':
        print_todos()
    elif select=='2':
        add_todo()
    elif select=='3':
        change_todo()
    elif select=='4':
        delete_todo()
    elif select=='999':
        print('종료')
        break