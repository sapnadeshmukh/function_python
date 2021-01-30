def fibonacci3(num):
    x=0
    y=1
    while x<num:
        print(x)
        z=x
        x=y
        y=z+y
        
user=int(input("enter num"))
fibonacci3(user)