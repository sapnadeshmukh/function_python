def factorial(num):

    i=1
    fact=1
    while(i<=num):
        fact=fact*i
        i=i+1
    print(fact)
user=int(input("enter num"))
factorial(user)