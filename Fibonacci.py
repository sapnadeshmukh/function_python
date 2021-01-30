def fibonacci(value):
    i=0
    j=1
    print(i)
    print(j)
    while(i<=value):
        k=i+j
        print(k)
        i=j
        j=k
    i=i+1
user=int(input("enter num"))
fibonacci(user)