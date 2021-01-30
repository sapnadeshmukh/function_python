def squareOfNum():
    new_list=[]
    user=int(input("enter num"))
    for i in range(1,user+1):
        
        new_list.append (i**2)
    print(new_list)
squareOfNum()

print("*******************************")

def squareOfNum():
    new_list=[]
    i=1
    while i<=30:
        new_list.append (i**2)
        i=i+1
    print(new_list)
squareOfNum()


print("******************************")

def perfectSquares( r): 
    l=1
    for i in range( l,r ): 
  
        if (i**(.5) == int(i**(.5))):   
            print(i, end=" ")
            
  
user=int(input("enter num to give range"))
  
perfectSquares( user) 


print("*******************************")




def perfectSquares( r): 
    i=1
    while i<=r:
  
        if (i**(.5) == int(i**(.5))):   
            print(i, end=" ")
        i=i+1
            
  
user=int(input("enter num to give range"))
  
perfectSquares( user) 









