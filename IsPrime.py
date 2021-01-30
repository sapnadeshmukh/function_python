def Is_Prime(num):

    i=2
    while(i<num):
        if(num%i==0):
            print(num,"not prime")
            break
        i=i+1
    else:
        print(num,"Prime number")
user=int (input("enter num"))
Is_Prime(user)

            
