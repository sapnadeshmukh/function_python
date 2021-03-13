
# by for loop
def find_max(numbers) :
    maxelement = numbers[0]
    for element in numbers :
        if element>maxelement :
            maxelement= element  
    return maxelement

marks=[-45,-88]
result = find_max(marks)
print(result)





# by while loop
def max_number(numbers):
    i=0
    max_num=numbers[i]
    while(i<len(numbers)):
        if numbers[i]>max_num:
            max_num=numbers[i]
        i=i+1
    return(max_num)
marks=[-4,-5,-7,-8,-9,-23]
result=max_number(marks)
print(result)
