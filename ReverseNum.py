def Reverse_Num(num):
    rev=0
    while (num>0):
        rem=num%10
        rev=rev*10+rem
        num=num//10
    print(rev)
user=int(input("enter a number"))
Reverse_Num(user)