#number is divisible by 3 = TIC
#number is divisible by 5 = TAC
#number 3,8 divisible by 5 =TIC TAC

#5%2=1 , 6%2=0
number1= int(input ('Enter number1'))
if (number1%3==0 and number1%5==0):
  print('TicTac')
elif (number1%5==0):
    print('Tac')
elif(number1%3==0):
    print('Tic')
else:
    print(number1)