i=1
a=0
new=[]
while(i<=3):
    # j=i
    empty_list1=[]
    p=1
    while(p<=10):
        k=i*p
        empty_list1.append(k)
        p=p+1
   
    a=i,empty_list1
    new.append(list(a))
    i=i+1
print(new)






