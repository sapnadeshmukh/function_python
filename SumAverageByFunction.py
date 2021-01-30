def Add():
    i=0
    sum=0
    average=0
    while (i<3):
        user=int(input("enter a number"))
        sum=sum+user
        i=i+1
    print (sum)
    average=sum//3
    print (average)        
Add()
