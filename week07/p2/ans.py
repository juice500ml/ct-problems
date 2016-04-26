def welcome():
    print('이 프로그램은 섭씨 온도를 화씨로, 화씨 온도를 섭씨로 바꿉니다')
    print('섭씨 온도를 화씨로 바꾸려면 (C) 를 입력하세요')
    print('화씨 온도를 섭씨로 바꾸려면 (F) 를 입력하세요')


def CtoF(start, end):
    print()
    print(' 섭씨온도', '  화씨온도')
    for temp in range(start, end+1):
        ftemp = (9/5 * temp) + 32
        print('''  %6.2f       %6.2f''' % (temp, ftemp))


def FtoC(start, end):
    print()
    print('화씨온도', ' 섭씨온도')
    for temp in range(start, end+1):
        ctemp = (temp-32) * 5/9
        print('%6.2f    %6.2f' % (temp, ctemp))
              

# main

welcome()
select = input('선택 ---> ')

if select == 'C':
    temp1 = int(input('섭씨 시작 온도를  입력하시오 : '))
    temp2 = int(input('섭씨 끝 온도를 입력하시오 : '))
    CtoF(temp1, temp2)
elif select == 'F':
    temp1 = int(input('화씨 시작 온도를  입력하시오 : '))
    temp2 = int(input('화씨 끝 온도를 입력하시오 : '))
    FtoC(temp1, temp2)
else:
    print('F 또는 C를 입력해야 합니다')
print()
print()
input('엔터를 누르면 프로그램이 끝납니다.')
print()
