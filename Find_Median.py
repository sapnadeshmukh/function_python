def find_median(a,b,c):
    m=0
    if (a>b):
        if (a<c):
            m=a
        elif(b>c):
            m=b
        else:
            m=c
    else:
        if (a>c):
            m=a
        elif(b<c):
            m=b
        else:
            m=c

    print("Median is =" ,m)
x=int(input("enter num"))
y=int(input("enter num"))
z=int(input("enter num"))
find_median(z,y,x)






