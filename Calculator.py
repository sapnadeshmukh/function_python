def calculator(num1,num2,operation):
    if (operation == "add"):
        add_result=(num1+num2)
        print(add_result)


    elif (operation == "subtract"):
        subtract_result=(num1-num2)
        print(subtract_result)

    elif (operation == "multiply"):
        multiply_result=(num1*num2)
        print (multiply_result)


    elif (operation == "divide"):
        divide_result=(num1//num2)
        print(divide_result)

number1=int(input("enter first number"))
number2=int(input("enter second number"))
operater=str(input("enter operation"))
calculator(number1,number2,operater)


def list_change(x,y):
    i=0
    new=[]
    while i<(len(x)):
        z=x[i]*y[i]
        new.append(z)
        i=i+1
    print(new)

list_change([5,10,50,20],[2,20,3,5])
