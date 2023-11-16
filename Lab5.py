number1= int(input ('Enter number1'))
if (number1%3==0 and number1%5==0):
  print('TicTac')
elif (number1%5==0):
    print('Tac')
elif(number1%3==0):
    print('Tic')


count=1
while(count<21):
    print(count,end=',')
    if (count % 3 == 0 and count % 5 == 0):
        print('TicTac')
    elif (count % 5 == 0):
        print('Tac')
    elif (count % 3 == 0):
        print('Tic')
    count=count+1

import random
print(random.randint(50, 100))
import random
tmpcount = 1
number2 = int(input('Enter Number2: '))

while number2 <= 0 and tmpcount < 5:
    number2 = int(input('Enter Value Greater than 0: '))
    print('Value of tmpcount:', tmpcount)
    tmpcount += 1
import random
tmp2 = random.randint(50, 100)
if tmp2 == number2:
    print('Perfect Match')
elif(tmp2!=number2):
    print(tmp2, number2)




