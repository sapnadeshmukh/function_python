def Perfect_Num(num):
    sum=0
    i=1
    while (i<num):
        if (num%i==0):
            sum=sum+i
        i=i+1
    if (sum==num):
        print (num,"Perfect Number")
    else:
        print(num,"Not Perfect Number")
user=int(input("enter number"))      
Perfect_Num(user)



print("*********************************************************************")

def Perfect_Number():
    num=1
    while (num<=1000):
        sum=0
        i=1
        while (i<(num)):
            if (num%i==0):
                sum=sum+i
            i=i+1
        if (sum==num):
            print (num,"Perfect Number")
        
        num=num+1
Perfect_Number()

