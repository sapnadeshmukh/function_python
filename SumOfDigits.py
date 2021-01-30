def sumofdigits(number):
    sum = 0
    modulus = 0
    while number>0 :
        modulus = number%10
        sum=sum+modulus
        number=number//10
    return sum
user=(int(input("enter a number")))
print(sumofdigits(user))
 