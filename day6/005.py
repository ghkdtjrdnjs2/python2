# bool
b1, b2, b3, b4 = True, True, True, False
# and : 모두 참
# or : 하나만 참이면 된다
print(b1 and b2 and b3) # 참

print(b1 and b2 and b4) # 거짓
print(b4 and b1 and b2) # 거짓

print(b1 or b2 or b4) # 참
print((b1 and b1) or (b4 or b1))

nai=30
gender='여자'
city='인천'
# 나이가 20이상이고 성별은 여자

nai>=20 and gender=='여자'
# 나이가 20이상이고 성별은 여자인 사람 또는 인천에 사는 사람
# 1.나이가 20이상이고 성별은 여자인 사람
# 2.인천에 사는 사람
# 둘 중 하나만 만족
(nai>=20 and gender=='여자') or city=='인천'

