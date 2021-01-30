def check_range(num):
    a=range(0,20)
    if (num in (a)):
        print(num,"yes, it is in range")
    else:
        print(num,"no,it is not in range")
user=int(input("enter num"))
check_range(user)