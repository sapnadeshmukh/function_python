def greatest_num(number1,number2,number3):
    if(number1> number2 and number1> number3):
        print(number1)
    elif(number2>number1 and number2>number3):
        print(number2)
    else:
        print(number3)


num1=int(input("enter 1st num"))
num2=int(input("enter 2nd num"))
num3=int(input("enter 3rd num"))
greatest_num(num1,num2,num3)