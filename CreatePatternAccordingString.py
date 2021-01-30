def series(list1,pattern):
    i=0
    new=[]
    while (i<len(list1)):
        if (list1[0] == list1[i]):
            new.append("a")
        elif(list1[1] == list1[i]):
            new.append("b")
        else:
            new.append("c")
        i=i+1
    print("correct output", new)
    if new==pattern:
        print("True")
    else:
        print("False")

a=int(input("enter how many element do you want "))
i=1
list2=[]
while (i<=a):
    ask=input("enter any string")
    list2.append(ask)
    i=i+1
print(list2)
b=int(input("enter how many pattern according to string" ))
i=1
list3=[]
while i<=b:
    ask2=input("enter any string")
    list3.append(ask2)
    i=i+1
print(list3)
print("output of user",list3)
series(list2,list3)

print("*********************************")
# taking list from user
def series(list1):
    i=0
    new=[]
    while (i<len(list1)):
        if (list1[0] == list1[i]):
            new.append("A")
        elif(list1[1] == list1[i]):
            new.append("B")
        else:
            new.append("C")
        i=i+1
    print( new)
a=int(input("enter how many element do you want "))
i=1
list2=[]
while (i<=a):
    ask=input("enter any string")
    list2.append(ask)
    i=i+1
print(list2)
series(list2)












    