def isGreaterThen20 (b,a=20):
    print(a + b)

isGreaterThen20(9)

print("**********************************************") 


def Students(*names):
    for i in names:
        print(i)
Students("sapna","sona","bittu")


print("**************************************************")

def  add_numbers(number1,number2):
    sum=number1+number2
    print (sum)
add_numbers(56,12)
print("***************************************************")


def add_numbers_list (list1,list2):
    i=0
    while (i<len(list1)):
        sum=list1[i]+list2[i]
        print(sum)
        i=i+1


add_numbers_list([1,2,3],[4,5,6])