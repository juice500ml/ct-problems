num = int(input('수를 입력하시오: '))
for i in range(1,num+1):
    print('*'*i)
print('')
for i in range(1,num+1):
    print(' '*(num-i) + '*'*i)
