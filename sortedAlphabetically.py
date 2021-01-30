def sortedSentence(Sentence): 
    words = Sentence.split("-")

    
    words.sort() 
    newSentence = "-".join(words) 
    return newSentence 
Sentence=input("enter any string")
print(sortedSentence(Sentence)) 
  
 
 


print("*****************************")


list=["red","green","yellow","white","blue"]
i=0
while (i<len(list)):
    j=i+1
    while(j<len(list)):
        if ((list[i]) > (list[j])):
            var=list[i]
            list[i]=list[j]
            list[j]=var
        j=j+1
    i=i+1
print(list)


