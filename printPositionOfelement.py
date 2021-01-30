
def Check_index(number):
    i=0
    max_num=0
    index=0
    while (i<len(number)):
        if (number[i]>max_num):
            max_num=number[i]
            index=i
        i=i+1
    print(max_num)
    print(index)

a=int(input("how many elements "))
i=0
num=[]
while(i<a):
    number=int(input("enter num"))
    num.append(number)
    i=i+1
Check_index(num)

    
