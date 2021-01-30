def max_num(numbers):
    i=0
    max=0
    while(i<len(numbers)):
        if numbers[i]>max:
            max=numbers[i]
        i=i+1
    return(max) 
def sum_of_max(x,y):
    new=[]
    a= max_num(x)
    new.append(a)       
    b= max_num(y)
    new.append(b)
    c=max_num(new)
    return (c)
list1=[4,6,9,12,34,6,98,121]
list2=[7,87,98,34,23,12,123,100]
result=sum_of_max(list1,list2)
print(result)
