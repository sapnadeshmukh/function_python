numbers=[1,2,3,4,5,6,7,8,9,10]
i=0
count_even=0
count_odd=0
even_list=[]
odd_list=[]
final_list=[]
while(i<len(numbers)):
    if (numbers[i]%2==0):
        even_list.append(numbers[i])
        count_even=count_even+1
        a=("even",count_even,even_list)
    else:
        odd_list.append(numbers[i])

        count_odd=count_odd+1
        b=("odd",count_odd,odd_list)

    i=i+1
final_list.append(list(a))
final_list.append(list(b))
print(final_list)


