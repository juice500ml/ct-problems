print('1 : 승차권+입장권 2: 입장권')
ticket = int(input('구입하실 표를 선택해 주세요 : '))
old = int(input('나이를 입력해 주세요 : '))

if ticket == 1:
    money = 8000
elif ticket == 2:
    money = 5000

if old <= 7:
    money = money/2

print('승차권의 가격은',money,'입니다')
