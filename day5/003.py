lang = 'python'
#slicing
print(lang[0])     #p
print(lang[5])     #n
print('a' in lang)
print('p' in lang)

#뒤에서 slicing
print(lang[-1])

string = '123456789'
# 문자열[시작위치:끝위치+1]
print(string[1:3])
# 문자열[시작위치:끝위치+1:간격]
print(string[1::5])
# 짝수만 출력
print(string[1::2])

# set(셋)은 슬라이싱 불가능
