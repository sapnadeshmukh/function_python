def showNumbers(limit) :
    i=0
    while(i<=limit):
        if(i%2==0):
            print(i ,"EVEN")
        else:
            print(i,"ODD")
        i=i+1
user=int(input("enter number"))
showNumbers(user)
