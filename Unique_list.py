def unique_list(element):
    i=0
    new_list=[]
    while (i<len(element)):
        if(element[i] not in (new_list)):
            new_list.append(element[i])
        i=i+1
    print(new_list)




unique_list([1,2,6,5,3,3,3,3,4,5])