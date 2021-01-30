def unique_list(element):
    i=0
    new=[]
    while (i<len(element)):
        if (element[i] not in new):
            new.append(element[i])
        i=i+1
    
    print(new)




list =([1,7,7,2,3,3,3,3,4,5,6,6])
unique_list(list)


