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
def take_list(n):
    even_list=[]
    odd_list=[]
    i=0
    while(i<len(n)):
        if (n[i]%2==0):
            even_list.append(n[i])
        else:
            odd_list.append(n[i])

        i=i+1
    print(even_list)
    print(odd_list)
    final_max=sum_of_max(even_list,odd_list)
    print(final_max)
big_list=[1,4,8,9,2,3,55,67,2,98,123,567,144]
take_list(big_list)

