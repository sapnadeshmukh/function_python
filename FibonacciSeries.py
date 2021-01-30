def fibonacci(num):
    i=0
    j=1
    print(i)
    print(j)
    count=2
    while (count<num):
        k=i+j
        count=count+1
        print(k)
        i=j
        j=k
user=int(input("enter num"))
fibonacci(user)


