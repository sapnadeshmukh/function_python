def check_even(list):
    i=0
    new_list=[]
    while(i<len(list)):
        if (list[i]%2==0):
            new_list.append(list[i])
        
        i=i+1
    print(new_list)




a=([1, 2, 3, 4, 5, 6, 7, 8, 9])
check_even(a)