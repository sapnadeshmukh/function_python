def check_numbers (a,b):
    if(a%2==0 and b%2==0):
        print("Dono even hai")
    else:
        print("Dono even  nahi hai")

check_numbers(4,8)




print("***********************************************************")

def check_numbers_list(list1,list2):
    i=0
    while(i<len(list1)):
        if (list1[i]%2==0 )and (list2[i]%2==0):
            print(list1[i] , "and " , list2[i], "Dono even hai" )
        else:
            print(list1[i] , "and"  ,list2[i] ,"Dono even nhi hai")

        i=i+1

check_numbers_list([2, 6, 18, 10, 3, 75] ,[6, 19, 24, 12, 3, 87])