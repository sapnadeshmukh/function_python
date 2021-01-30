def primeorNot(num):     
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                break
            

        else:
           print(num,"prime number")
primeorNot(402) 
