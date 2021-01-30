def max_number(numbers):
    i=0
    max_num=0
    while(i<len(numbers)):
        if numbers[i]>max_num:
            max_num=numbers[i]
        i=i+1
    return(max_num) 
def sum_of_max(x,y):
    c=x+y
    d=max_number(c)
    return(d)
list1=[4,6,9,12,34,6,98,121,143]
list2=[7,87,98,34,23,12,100,122]
result=sum_of_max(list1,list2)
print(result)
