def Speed_Name(speed):
    point=0
    if (speed<70):
        print("OK")
    elif (speed >70):
        i=71
        while (i<= speed):
            point=point+1
            i=i+5
        print("point :" ,point)
    if (point >12):
        print("License suspended")
user=int(input("enter num"))
Speed_Name(user)






